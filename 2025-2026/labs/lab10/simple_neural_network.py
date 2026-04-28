import random
from typing import Dict, Any, Tuple

import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

from players import RLAgent


class SimpleNN(nn.Module):
    def __init__(self, in_features, out_features, hidden):
        super().__init__()
        self.layers = nn.ModuleList([
            nn.Linear(in_features, hidden),
            nn.Linear(hidden, hidden),
            nn.Linear(hidden, hidden),
            nn.Linear(hidden, hidden),
            nn.Linear(hidden, hidden),
            nn.Linear(hidden, hidden),
            nn.Linear(hidden, out_features),
        ])

    def forward(self, x):
        x = x.to('cuda' if torch.cuda.is_available() else 'cpu')
        for i in range(len(self.layers) - 1):
            x = self.layers[i](x)
            x = F.relu(x)
        x = self.layers[-1](x)

        return x


class CNN(nn.Module):
    def __init__(self):
        super().__init__()

        self.conv_layers = nn.ModuleList([
            # 20 x 10
            nn.Conv2d(1, 64, 3, padding = 1), # 20 x 10
            nn.Conv2d(64, 16, (20, 1)), # 1 x 10
        ])

        self.merging_layers = nn.ModuleList([
            nn.Linear(16 * 1 * 10 + 14, 128),

        ])

        self.out_layers = nn.ModuleList([
            nn.Linear(128, 40),
        ])

    def forward(self, x):
        x = x.to('cuda' if torch.cuda.is_available() else 'cpu')
        x1, x2 = torch.split(x, [200, 14])
        x1 = x1.view([1, 20, 10])

        for layer in self.conv_layers:
            x1 = layer(x1)
            x1 = F.relu(x1)

        x1 = x1.view([-1])
        x = torch.cat([x1, x2])
        for layer in self.merging_layers:
            x = layer(x)
            x = F.relu(x)

        for layer in self.out_layers:
            x = layer(x)

        return x


class SimpleNNAgent(RLAgent):
    def __init__(self, name: str = "RL Agent", exploration_rate: float = 0.1, pretrained = False):
        super().__init__(name, exploration_rate)
        # self.model = SimpleNN(214, 40, 256).to('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = CNN().to('cuda' if torch.cuda.is_available() else 'cpu')

        if pretrained:
            self.model.load_state_dict(torch.load('model.pt', weights_only=False))
            self.set_training_mode(False)

        # extra info to remember
        self.episode_input = []
        self.episode_action_id = []
        self.episode_input_to_remember = None
        self.episode_action_id_to_remember = None

        self.optimizer = torch.optim.Adam(self.model.parameters(), lr = 0.001)

    @staticmethod
    def _board_state_to_input(state: Dict[str, Any]) -> np.ndarray:
        ''' turns state dictionary into an array of usable inputs '''

        board = state['board']
        current_piece = state['current_piece']
        next_piece = state['next_piece']

        # The CNN architecture is fixed to a 20x10 board (40 = 10 cols * 4 rotations outputs).
        if board.shape != (20, 10):
            raise ValueError(
                f"SimpleNNAgent/CNN only supports a 20x10 board, got {board.shape}. "
                "Run with --width 10 --height 20 or use a different agent."
            )

        piece_type = {'I' : 0, 'O' : 1, 'L' : 2, 'J' : 3, 'Z' : 4, 'S' : 5, 'T' : 6}
        current_piece_v = [0.0 for _ in range(7)]
        current_piece_v[piece_type[current_piece]] = 1.0
        next_piece_v = [0.0 for _ in range(7)]
        next_piece_v[piece_type[next_piece]] = 1.0

        input_vals = np.append(np.array(board.flatten(), dtype = 'bool'), [current_piece_v, next_piece_v])
        return input_vals

    def remember_extra(self, input_params, action_id):
        self.episode_input_to_remember = input_params
        self.episode_action_id_to_remember = action_id

    def remember(self, state, action, reward):
        super().remember(state, action, reward)
        self.episode_input.append(self.episode_input_to_remember)
        self.episode_action_id.append(self.episode_action_id_to_remember)

    def get_best_action(self, state: Dict[str, Any]) -> Tuple[int, int]:
        input_params = self._board_state_to_input(state)

        predictions = self.model.forward(torch.FloatTensor(input_params))

        valid_actions = state['valid_actions']
        max_pos = 0
        max_pred = predictions[0]
        for i, prediction in enumerate(predictions):
            col, rotation = i // 4, i % 4
            if (col, rotation) not in valid_actions:
                continue
            if prediction > max_pred:
                max_pred = prediction
                max_pos = i

        action = max_pos // 4, max_pos % 4
        self.remember_extra(input_params, max_pos)

        return action

    def train(self, decay_factor = 0.5):
        for i in range(len(self.episode_rewards) - 2, -1, -1):
            self.episode_rewards[i] += decay_factor * self.episode_rewards[i + 1]

        self.optimizer.zero_grad()

        for episode in range(len(self.episode_states)):
            input_params = self.episode_input[episode]
            output = self.model.forward(torch.FloatTensor(input_params))
            action_id = self.episode_action_id[episode]
            ((output[action_id] - self.episode_rewards[episode]) ** 2).backward()

        self.optimizer.step()
        # self.exploration_rate -= 0.00003

        self.clear_episode()

    def clear_episode(self):
        super().clear_episode()
        self.episode_input.clear()
        self.episode_action_id.clear()

    @staticmethod
    def _count_holes(board):

        hole_count = 0
        for j in range(10):
            roof = False
            for i in range(20):
                if board[i][j]:
                    roof = True
                elif roof:
                  hole_count += 1

        return hole_count

    @staticmethod
    def _compute_height_penalty(board):
        # print(board)
        penalty = 0
        for j in range(10):
            for i in range(20):
                penalty += (20 - i) * (board[i][j] > 0)

        return penalty

    @staticmethod
    def _measure_frontier(board):
        # measures the perimeter of the filled part of the board

        changes = 0
        for j in range(10):
            for i in range(1, 20):
                if bool(board[i][j]) != bool(board[i-1][j]):
                    changes += 1
        for i in range(20):
            for j in range(1, 10):
                if bool(board[i][j]) != bool(board[i][j-1]):
                    changes += 1

        return changes

    def calculate_reward(self, prev_state: Dict, new_state: Dict, game_over: bool) -> float:
        """
        Calculate reward for state transition.

        Args:
            prev_state: Previous game state
            new_state: New game state
            game_over: Whether game ended

        Returns:
            Reward value
        """
        reward = 0.0
        if game_over:
            # point penalty for losing
            reward -= 500
            pass

        # reward for not dying
        reward += 5

        reward -= self._compute_height_penalty(new_state['board']) - self._compute_height_penalty(prev_state['board'])
        # reward -= 5 * (self._count_holes(new_state['board']) - self._compute_height_penalty(prev_state['board']))
        reward -= 3 * (self._measure_frontier(new_state['board']) - self._measure_frontier(prev_state['board']))

        # Reward for increasing score
        reward += 10.0 * (new_state['score'] - prev_state['score'])

        return reward

    def choose_action(self, state: Dict[str, Any]) -> Tuple[int, int]:
        """
        Choose action with exploration-exploitation.

        Args:
            state: Current game state

        Returns:
            (column, rotation) action
        """
        valid_actions = state['valid_actions']
        if not valid_actions:
            return 0, 0

        # Exploration
        if self.training_mode and random.random() < self.exploration_rate:
            random_action = random.choice(valid_actions)

            column, rotation = random_action
            input_params = self._board_state_to_input(state)
            self.remember_extra(input_params, column * 4 + rotation)
            return random_action

        # Exploitation
        return self.get_best_action(state)

    def save_model(self):
        torch.save(self.model.state_dict(), 'model.pt')