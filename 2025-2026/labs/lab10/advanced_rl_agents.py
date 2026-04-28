import random
from typing import Dict, Any, Tuple, List
from collections import deque
import numpy as np

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

from players import RLAgent


class DQNetwork(nn.Module):

    def __init__(self, state_size: int = 214, action_size: int = 40, hidden_size: int = 256):
        super(DQNetwork, self).__init__()
        self.fc1 = nn.Linear(state_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, hidden_size)
        self.fc4 = nn.Linear(hidden_size, action_size)

    def forward(self, x):
        x = x.to('cuda' if torch.cuda.is_available() else 'cpu')
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = self.fc4(x)
        return x


class DuelingDQNetwork(nn.Module):
    def __init__(self, state_size: int = 214, action_size: int = 40, hidden_size: int = 256):
        super(DuelingDQNetwork, self).__init__()

        # Shared feature extraction layers
        self.feature = nn.Sequential(
            nn.Linear(state_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, hidden_size),
            nn.ReLU()
        )

        # Value stream
        self.value_stream = nn.Sequential(
            nn.Linear(hidden_size, hidden_size // 2),
            nn.ReLU(),
            nn.Linear(hidden_size // 2, 1)
        )

        # Advantage stream
        self.advantage_stream = nn.Sequential(
            nn.Linear(hidden_size, hidden_size // 2),
            nn.ReLU(),
            nn.Linear(hidden_size // 2, action_size)
        )

    def forward(self, x):
        x = x.to('cuda' if torch.cuda.is_available() else 'cpu')
        features = self.feature(x)
        value = self.value_stream(features)
        advantages = self.advantage_stream(features)

        # Q(s,a) = V(s) + (A(s,a) - mean(A(s,a)))
        q_values = value + (advantages - advantages.mean(dim=-1, keepdim=True))
        return q_values


class PolicyNetwork(nn.Module):
    """Policy network for policy gradient methods."""

    def __init__(self, state_size: int = 214, action_size: int = 40, hidden_size: int = 256):
        super(PolicyNetwork, self).__init__()
        self.fc1 = nn.Linear(state_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, action_size)

    def forward(self, x):
        x = x.to('cuda' if torch.cuda.is_available() else 'cpu')
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        # Softmax to get probability distribution over actions
        x = F.softmax(self.fc3(x), dim=-1)
        return x


class DQNAgent(RLAgent):
    """
    Deep Q-Network (DQN) Agent with Experience Replay and Target Network.

    Key concepts:
    - Experience Replay: Store past experiences and sample randomly to break correlation
    - Target Network: Separate network for stable Q-value targets
    - Epsilon-greedy: Balance exploration and exploitation
    """

    def __init__(self,
                 name: str = "DQN Agent",
                 state_size: int = 214,
                 action_size: int = 40,
                 hidden_size: int = 256,
                 learning_rate: float = 0.001,
                 gamma: float = 0.95,
                 epsilon_start: float = 1.0,
                 epsilon_end: float = 0.01,
                 epsilon_decay: float = 0.995,
                 memory_size: int = 10000,
                 batch_size: int = 64,
                 target_update_freq: int = 10):

        super().__init__(name, exploration_rate=epsilon_start)

        self.state_size = state_size
        self.action_size = action_size
        self.gamma = gamma
        self.epsilon = epsilon_start
        self.epsilon_end = epsilon_end
        self.epsilon_decay = epsilon_decay
        self.batch_size = batch_size
        self.target_update_freq = target_update_freq
        self.learn_step_counter = 0

        # Device
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        # Q-Networks
        self.policy_net = DQNetwork(state_size, action_size, hidden_size).to(self.device)
        self.target_net = DQNetwork(state_size, action_size, hidden_size).to(self.device)
        self.target_net.load_state_dict(self.policy_net.state_dict())
        self.target_net.eval()

        # Optimizer
        self.optimizer = optim.Adam(self.policy_net.parameters(), lr=learning_rate)

        # Experience Replay Memory: stores (state, action, reward, next_state, done)
        self.memory = deque(maxlen=memory_size)

        # For tracking
        self.losses = []

    def board_state_to_input(self, state: Dict[str, Any]) -> np.ndarray:
        """Convert game state to neural network input."""
        board = state['board']
        current_piece = state['current_piece']
        next_piece = state['next_piece']

        piece_type = {'I': 0, 'O': 1, 'L': 2, 'J': 3, 'Z': 4, 'S': 5, 'T': 6}
        current_piece_v = [0.0] * 7
        current_piece_v[piece_type[current_piece]] = 1.0
        next_piece_v = [0.0] * 7
        next_piece_v[piece_type[next_piece]] = 1.0

        input_vals = np.append(
            np.array(board.flatten(), dtype='float32'),
            current_piece_v + next_piece_v
        )
        return input_vals

    def get_best_action(self, state: Dict[str, Any]) -> Tuple[int, int]:
        """Get best action using policy network."""
        input_params = self.board_state_to_input(state)

        with torch.no_grad():
            state_tensor = torch.FloatTensor(input_params).unsqueeze(0).to(self.device)
            q_values = self.policy_net(state_tensor).squeeze()

        valid_actions = state['valid_actions']

        # Find best valid action
        best_action = None
        best_q = float('-inf')

        for col in range(10):
            for rot in range(4):
                if (col, rot) in valid_actions:
                    action_idx = col * 4 + rot
                    q_val = q_values[action_idx].item()
                    if q_val > best_q:
                        best_q = q_val
                        best_action = (col, rot)

        return best_action if best_action else valid_actions[0]

    def choose_action(self, state: Dict[str, Any]) -> Tuple[int, int]:
        """Choose action with epsilon-greedy policy."""
        valid_actions = state['valid_actions']
        if not valid_actions:
            return (0, 0)

        # Update exploration rate
        self.exploration_rate = self.epsilon

        # Epsilon-greedy
        if self.training_mode and random.random() < self.epsilon:
            return random.choice(valid_actions)
        else:
            return self.get_best_action(state)

    def remember(self, state: np.ndarray, action: Tuple[int, int], reward: float,
                 next_state: np.ndarray = None, done: bool = False):
        """Store experience in replay memory."""
        if self.training_mode:
            action_idx = action[0] * 4 + action[1]
            self.memory.append((state, action_idx, reward, next_state, done))

    def train(self):
        """Train the network using experience replay."""
        if len(self.memory) < self.batch_size:
            return

        # Sample random batch from memory
        batch = random.sample(self.memory, self.batch_size)
        states, actions, rewards, next_states, dones = zip(*batch)

        # Convert to tensors
        states = torch.FloatTensor(np.array(states)).to(self.device)
        actions = torch.LongTensor(actions).to(self.device)
        rewards = torch.FloatTensor(rewards).to(self.device)
        dones = torch.FloatTensor(dones).to(self.device)

        # Handle next_states (some might be None if episode ended)
        non_final_mask = torch.tensor([s is not None for s in next_states],
                                      dtype=torch.bool, device=self.device)
        non_final_next_states = torch.FloatTensor(
            np.array([s for s in next_states if s is not None])
        ).to(self.device)

        # Current Q values
        current_q_values = self.policy_net(states).gather(1, actions.unsqueeze(1)).squeeze()

        # Target Q values
        next_q_values = torch.zeros(self.batch_size, device=self.device)
        with torch.no_grad():
            if non_final_mask.any():
                next_q_values[non_final_mask] = self.target_net(non_final_next_states).max(1)[0]

        target_q_values = rewards + (self.gamma * next_q_values * (1 - dones))

        # Compute loss
        loss = F.mse_loss(current_q_values, target_q_values)

        # Optimize
        self.optimizer.zero_grad()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(self.policy_net.parameters(), 1.0)
        self.optimizer.step()

        self.losses.append(loss.item())
        self.learn_step_counter += 1

        # Update target network
        if self.learn_step_counter % self.target_update_freq == 0:
            self.target_net.load_state_dict(self.policy_net.state_dict())

        # Decay epsilon
        self.epsilon = max(self.epsilon_end, self.epsilon * self.epsilon_decay)

        # Clear episode memory
        self.clear_episode()

    def calculate_reward(self, prev_state: Dict, new_state: Dict, game_over: bool) -> float:
        """Calculate reward for state transition."""
        reward = 0.0

        if game_over:
            reward -= 100
        else:
            reward += 1  # Survival bonus

        # Reward for clearing lines (exponential)
        lines_cleared = new_state['lines_cleared'] - prev_state['lines_cleared']
        if lines_cleared > 0:
            reward += lines_cleared ** 2 * 10

        # Penalty for height increase
        prev_height = self._get_max_height(prev_state['board'])
        new_height = self._get_max_height(new_state['board'])
        reward -= max(0, new_height - prev_height) * 2

        # Penalty for holes
        holes_created = self._count_holes(new_state['board']) - self._count_holes(prev_state['board'])
        reward -= holes_created * 5

        return reward

    def _count_holes(self, board: np.ndarray) -> int:
        """Count holes in the board."""
        holes = 0
        height, width = board.shape
        for col in range(width):
            found_block = False
            for row in range(height):
                if board[row, col] != 0:
                    found_block = True
                elif found_block:
                    holes += 1
        return holes


class DoubleDQNAgent(DQNAgent):
    """
    Double DQN Agent - addresses overestimation bias in standard DQN.

    Key difference from DQN:
    - Uses policy network to SELECT action
    - Uses target network to EVALUATE action
    - Reduces overoptimistic Q-value estimates
    """

    def __init__(self, name: str = "Double DQN Agent", **kwargs):
        super().__init__(name, **kwargs)

    def train(self):
        """Train using Double DQN update rule."""
        if len(self.memory) < self.batch_size:
            return

        batch = random.sample(self.memory, self.batch_size)
        states, actions, rewards, next_states, dones = zip(*batch)

        states = torch.FloatTensor(np.array(states)).to(self.device)
        actions = torch.LongTensor(actions).to(self.device)
        rewards = torch.FloatTensor(rewards).to(self.device)
        dones = torch.FloatTensor(dones).to(self.device)

        non_final_mask = torch.tensor([s is not None for s in next_states],
                                      dtype=torch.bool, device=self.device)
        non_final_next_states = torch.FloatTensor(
            np.array([s for s in next_states if s is not None])
        ).to(self.device)

        # Current Q values
        current_q_values = self.policy_net(states).gather(1, actions.unsqueeze(1)).squeeze()

        # Double DQN: use policy net to select, target net to evaluate
        next_q_values = torch.zeros(self.batch_size, device=self.device)
        with torch.no_grad():
            if non_final_mask.any():
                # Select actions using policy network
                next_actions = self.policy_net(non_final_next_states).argmax(1)
                # Evaluate using target network
                next_q_values[non_final_mask] = self.target_net(non_final_next_states).gather(
                    1, next_actions.unsqueeze(1)
                ).squeeze()

        target_q_values = rewards + (self.gamma * next_q_values * (1 - dones))

        # Compute loss and update
        loss = F.mse_loss(current_q_values, target_q_values)

        self.optimizer.zero_grad()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(self.policy_net.parameters(), 1.0)
        self.optimizer.step()

        self.losses.append(loss.item())
        self.learn_step_counter += 1

        if self.learn_step_counter % self.target_update_freq == 0:
            self.target_net.load_state_dict(self.policy_net.state_dict())

        self.epsilon = max(self.epsilon_end, self.epsilon * self.epsilon_decay)
        self.clear_episode()


class DuelingDQNAgent(DQNAgent):
    """
    Dueling DQN - separates state value and action advantage.

    Key concept:
    - Q(s,a) = V(s) + A(s,a)
    - V(s): How good is this state?
    - A(s,a): How much better is action a compared to others?
    - More efficient learning in states where action choice doesn't matter much
    """

    def __init__(self, name: str = "Dueling DQN Agent", **kwargs):
        super().__init__(name, **kwargs)

        # Replace networks with Dueling architecture
        hidden_size = kwargs.get('hidden_size', 256)
        self.policy_net = DuelingDQNetwork(
            self.state_size, self.action_size, hidden_size
        ).to(self.device)
        self.target_net = DuelingDQNetwork(
            self.state_size, self.action_size, hidden_size
        ).to(self.device)
        self.target_net.load_state_dict(self.policy_net.state_dict())
        self.target_net.eval()

        # Update optimizer
        learning_rate = kwargs.get('learning_rate', 0.001)
        self.optimizer = optim.Adam(self.policy_net.parameters(), lr=learning_rate)


# ============================================================================
# POLICY GRADIENT AGENT (REINFORCE)
# ============================================================================

class REINFORCEAgent(RLAgent):
    """
    REINFORCE Policy Gradient Agent.

    Key concepts:
    - Directly learns policy π(a|s) instead of value function
    - Samples actions from probability distribution
    - Updates policy to increase probability of good actions
    - Uses Monte Carlo returns (complete episodes)
    """

    def __init__(self,
                 name: str = "REINFORCE Agent",
                 state_size: int = 214,
                 action_size: int = 40,
                 hidden_size: int = 256,
                 learning_rate: float = 0.001,
                 gamma: float = 0.99):

        super().__init__(name, exploration_rate=0.0)  # No epsilon-greedy needed

        self.state_size = state_size
        self.action_size = action_size
        self.gamma = gamma

        # Device
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        # Policy Network
        self.policy_net = PolicyNetwork(state_size, action_size, hidden_size).to(self.device)
        self.optimizer = optim.Adam(self.policy_net.parameters(), lr=learning_rate)

        # Episode storage
        self.episode_states = []
        self.episode_actions = []
        self.episode_rewards = []
        self.episode_log_probs = []

    def board_state_to_input(self, state: Dict[str, Any]) -> np.ndarray:
        """Convert game state to neural network input."""
        board = state['board']
        current_piece = state['current_piece']
        next_piece = state['next_piece']

        piece_type = {'I': 0, 'O': 1, 'L': 2, 'J': 3, 'Z': 4, 'S': 5, 'T': 6}
        current_piece_v = [0.0] * 7
        current_piece_v[piece_type[current_piece]] = 1.0
        next_piece_v = [0.0] * 7
        next_piece_v[piece_type[next_piece]] = 1.0

        input_vals = np.append(
            np.array(board.flatten(), dtype='float32'),
            current_piece_v + next_piece_v
        )
        return input_vals

    def get_best_action(self, state: Dict[str, Any]) -> Tuple[int, int]:
        """Sample action from policy (stochastic policy)."""
        input_params = self.board_state_to_input(state)
        state_tensor = torch.FloatTensor(input_params).unsqueeze(0).to(self.device)

        # Get action probabilities
        action_probs = self.policy_net(state_tensor).squeeze()

        valid_actions = state['valid_actions']

        # Create mask for valid actions
        mask = torch.zeros(self.action_size, device=self.device)
        for col, rot in valid_actions:
            action_idx = col * 4 + rot
            mask[action_idx] = 1.0

        # Apply mask and renormalize
        masked_probs = action_probs * mask
        masked_probs = masked_probs / (masked_probs.sum() + 1e-10)

        # Sample action
        if self.training_mode:
            action_dist = torch.distributions.Categorical(masked_probs)
            action_idx = action_dist.sample()
            log_prob = action_dist.log_prob(action_idx)

            # Store log probability for training
            self.episode_log_probs.append(log_prob)
        else:
            # During evaluation, pick highest probability
            action_idx = masked_probs.argmax()

        col = action_idx.item() // 4
        rot = action_idx.item() % 4

        return (col, rot)

    def remember(self, state: np.ndarray, action: Tuple[int, int], reward: float):
        """Store experience. REINFORCE trains from log-probs + rewards, so
        we just keep the raw state vector that choose_action already encoded."""
        if self.training_mode:
            self.episode_states.append(state)
            self.episode_actions.append(action)
            self.episode_rewards.append(reward)

    def train(self):
        """Train policy using REINFORCE algorithm."""
        if len(self.episode_rewards) == 0:
            return

        # Calculate discounted returns
        returns = []
        G = 0
        for reward in reversed(self.episode_rewards):
            G = reward + self.gamma * G
            returns.insert(0, G)

        # Normalize returns for stability
        returns = torch.FloatTensor(returns).to(self.device)
        returns = (returns - returns.mean()) / (returns.std() + 1e-10)

        # Calculate policy loss
        policy_loss = []
        for log_prob, G in zip(self.episode_log_probs, returns):
            policy_loss.append(-log_prob * G)

        # Update policy
        self.optimizer.zero_grad()
        loss = torch.stack(policy_loss).sum()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(self.policy_net.parameters(), 1.0)
        self.optimizer.step()

        # Clear episode
        self.episode_states.clear()
        self.episode_actions.clear()
        self.episode_rewards.clear()
        self.episode_log_probs.clear()

    def calculate_reward(self, prev_state: Dict, new_state: Dict, game_over: bool) -> float:
        """Calculate reward."""
        reward = 0.0

        if game_over:
            reward -= 50
        else:
            reward += 0.5

        lines_cleared = new_state['lines_cleared'] - prev_state['lines_cleared']
        if lines_cleared > 0:
            reward += lines_cleared ** 2 * 20

        prev_height = self._get_max_height(prev_state['board'])
        new_height = self._get_max_height(new_state['board'])
        reward -= max(0, new_height - prev_height) * 1.5

        return reward


class ActorCritic(nn.Module):
    """Actor-Critic network architecture."""

    def __init__(self, state_size: int = 214, action_size: int = 40, hidden_size: int = 256):
        super(ActorCritic, self).__init__()

        # Shared layers
        self.shared = nn.Sequential(
            nn.Linear(state_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, hidden_size),
            nn.ReLU()
        )

        # Actor head (policy)
        self.actor = nn.Linear(hidden_size, action_size)

        # Critic head (value function)
        self.critic = nn.Linear(hidden_size, 1)

    def forward(self, x):
        x = x.to('cuda' if torch.cuda.is_available() else 'cpu')
        shared_features = self.shared(x)

        action_probs = F.softmax(self.actor(shared_features), dim=-1)
        state_value = self.critic(shared_features)

        return action_probs, state_value


class A2CAgent(RLAgent):
    """
    Advantage Actor-Critic (A2C) Agent.

    Key concepts:
    - Actor: Learns policy π(a|s)
    - Critic: Learns value function V(s)
    - Advantage: A(s,a) = Q(s,a) - V(s)
    - Reduces variance compared to pure policy gradient
    """

    def __init__(self,
                 name: str = "A2C Agent",
                 state_size: int = 214,
                 action_size: int = 40,
                 hidden_size: int = 256,
                 learning_rate: float = 0.001,
                 gamma: float = 0.99,
                 value_coef: float = 0.5,
                 entropy_coef: float = 0.01):

        super().__init__(name, exploration_rate=0.0)

        self.gamma = gamma
        self.value_coef = value_coef
        self.entropy_coef = entropy_coef

        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        # Actor-Critic Network
        self.ac_net = ActorCritic(state_size, action_size, hidden_size).to(self.device)
        self.optimizer = optim.Adam(self.ac_net.parameters(), lr=learning_rate)

        # Episode storage
        self.episode_log_probs = []
        self.episode_values = []
        self.episode_rewards = []
        self.episode_entropies = []

    def board_state_to_input(self, state: Dict[str, Any]) -> np.ndarray:
        """Convert game state to neural network input."""
        board = state['board']
        current_piece = state['current_piece']
        next_piece = state['next_piece']

        piece_type = {'I': 0, 'O': 1, 'L': 2, 'J': 3, 'Z': 4, 'S': 5, 'T': 6}
        current_piece_v = [0.0] * 7
        current_piece_v[piece_type[current_piece]] = 1.0
        next_piece_v = [0.0] * 7
        next_piece_v[piece_type[next_piece]] = 1.0

        return np.append(
            np.array(board.flatten(), dtype='float32'),
            current_piece_v + next_piece_v
        )

    def get_best_action(self, state: Dict[str, Any]) -> Tuple[int, int]:
        """Sample action from policy."""
        input_params = self.board_state_to_input(state)
        state_tensor = torch.FloatTensor(input_params).unsqueeze(0).to(self.device)

        action_probs, state_value = self.ac_net(state_tensor)
        action_probs = action_probs.squeeze()

        valid_actions = state['valid_actions']

        # Mask invalid actions
        mask = torch.zeros(40, device=self.device)
        for col, rot in valid_actions:
            mask[col * 4 + rot] = 1.0

        masked_probs = action_probs * mask
        masked_probs = masked_probs / (masked_probs.sum() + 1e-10)

        if self.training_mode:
            action_dist = torch.distributions.Categorical(masked_probs)
            action_idx = action_dist.sample()

            # Store for training
            self.episode_log_probs.append(action_dist.log_prob(action_idx))
            self.episode_values.append(state_value)
            self.episode_entropies.append(action_dist.entropy())
        else:
            action_idx = masked_probs.argmax()

        return (action_idx.item() // 4, action_idx.item() % 4)

    def remember(self, state: np.ndarray, action: Tuple[int, int], reward: float):
        """Store reward."""
        if self.training_mode:
            self.episode_rewards.append(reward)

    def train(self):
        """Train using A2C update."""
        if len(self.episode_rewards) == 0:
            return

        # Calculate returns
        returns = []
        G = 0
        for reward in reversed(self.episode_rewards):
            G = reward + self.gamma * G
            returns.insert(0, G)

        returns = torch.FloatTensor(returns).to(self.device)
        returns = (returns - returns.mean()) / (returns.std() + 1e-10)

        # Calculate advantages
        values = torch.cat(self.episode_values).squeeze()
        advantages = returns - values.detach()

        # Policy loss (actor)
        policy_loss = []
        for log_prob, advantage in zip(self.episode_log_probs, advantages):
            policy_loss.append(-log_prob * advantage)
        policy_loss = torch.stack(policy_loss).sum()

        # Value loss (critic)
        value_loss = F.mse_loss(values, returns)

        # Entropy bonus (encourages exploration)
        entropy_loss = -torch.stack(self.episode_entropies).sum()

        # Total loss
        loss = policy_loss + self.value_coef * value_loss + self.entropy_coef * entropy_loss

        # Update
        self.optimizer.zero_grad()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(self.ac_net.parameters(), 1.0)
        self.optimizer.step()

        # Clear episode
        self.episode_log_probs.clear()
        self.episode_values.clear()
        self.episode_rewards.clear()
        self.episode_entropies.clear()

    def calculate_reward(self, prev_state: Dict, new_state: Dict, game_over: bool) -> float:
        """Calculate reward."""
        reward = 0.0

        if game_over:
            reward -= 50
        else:
            reward += 1

        lines_cleared = new_state['lines_cleared'] - prev_state['lines_cleared']
        if lines_cleared > 0:
            reward += lines_cleared ** 2 * 15

        prev_height = self._get_max_height(prev_state['board'])
        new_height = self._get_max_height(new_state['board'])
        reward -= max(0, new_height - prev_height) * 2

        return reward


class PrioritizedReplayBuffer:
    """
    Prioritized Experience Replay Buffer.

    Samples experiences based on their TD error - experiences with
    higher errors are more important for learning.
    """

    def __init__(self, capacity: int, alpha: float = 0.6):
        self.capacity = capacity
        self.alpha = alpha  # How much prioritization to use
        self.buffer = []
        self.priorities = []
        self.position = 0

    def add(self, experience, td_error: float = None):
        """Add experience with priority."""
        max_priority = max(self.priorities) if self.priorities else 1.0

        if len(self.buffer) < self.capacity:
            self.buffer.append(experience)
            self.priorities.append(max_priority)
        else:
            self.buffer[self.position] = experience
            self.priorities[self.position] = max_priority

        self.position = (self.position + 1) % self.capacity

    def sample(self, batch_size: int, beta: float = 0.4):
        """Sample batch with priorities."""
        if len(self.buffer) < batch_size:
            return None, None, None

        # Calculate sampling probabilities
        priorities = np.array(self.priorities[:len(self.buffer)])
        probs = priorities ** self.alpha
        probs /= probs.sum()

        # Sample indices
        indices = np.random.choice(len(self.buffer), batch_size, p=probs, replace=False)

        # Calculate importance sampling weights
        weights = (len(self.buffer) * probs[indices]) ** (-beta)
        weights /= weights.max()  # Normalize

        # Get experiences
        experiences = [self.buffer[idx] for idx in indices]

        return experiences, indices, weights

    def update_priorities(self, indices, td_errors):
        """Update priorities based on TD errors."""
        for idx, td_error in zip(indices, td_errors):
            self.priorities[idx] = abs(td_error) + 1e-6

    def __len__(self):
        return len(self.buffer)


class PrioritizedDQNAgent(DQNAgent):
    """
    DQN with Prioritized Experience Replay.

    Key concept:
    - Not all experiences are equally valuable
    - Sample experiences where TD error is high (more to learn)
    - Use importance sampling weights to correct bias
    """

    def __init__(self, name: str = "Prioritized DQN", **kwargs):
        super().__init__(name, **kwargs)

        # Replace regular memory with prioritized buffer
        memory_size = kwargs.get('memory_size', 10000)
        self.memory = PrioritizedReplayBuffer(memory_size, alpha=0.6)
        self.beta_start = 0.4
        self.beta_frames = 100000
        self.frame = 0

    def remember(self, state: np.ndarray, action: Tuple[int, int], reward: float,
                 next_state: np.ndarray = None, done: bool = False):
        """Store experience in prioritized buffer."""
        if self.training_mode:
            action_idx = action[0] * 4 + action[1]
            experience = (state, action_idx, reward, next_state, done)
            self.memory.add(experience)

    def train(self):
        """Train using prioritized experience replay."""
        if len(self.memory) < self.batch_size:
            return

        # Update beta for importance sampling
        self.frame += 1
        beta = min(1.0, self.beta_start + self.frame * (1.0 - self.beta_start) / self.beta_frames)

        # Sample prioritized batch
        batch_data = self.memory.sample(self.batch_size, beta)
        if batch_data[0] is None:
            return

        experiences, indices, weights = batch_data
        states, actions, rewards, next_states, dones = zip(*experiences)

        # Convert to tensors
        states = torch.FloatTensor(np.array(states)).to(self.device)
        actions = torch.LongTensor(actions).to(self.device)
        rewards = torch.FloatTensor(rewards).to(self.device)
        dones = torch.FloatTensor(dones).to(self.device)
        weights = torch.FloatTensor(weights).to(self.device)

        non_final_mask = torch.tensor([s is not None for s in next_states],
                                      dtype=torch.bool, device=self.device)
        non_final_next_states = torch.FloatTensor(
            np.array([s for s in next_states if s is not None])
        ).to(self.device)

        # Current Q values
        current_q_values = self.policy_net(states).gather(1, actions.unsqueeze(1)).squeeze()

        # Target Q values
        next_q_values = torch.zeros(self.batch_size, device=self.device)
        with torch.no_grad():
            if non_final_mask.any():
                next_q_values[non_final_mask] = self.target_net(non_final_next_states).max(1)[0]

        target_q_values = rewards + (self.gamma * next_q_values * (1 - dones))

        # Calculate TD errors for priority update
        td_errors = (current_q_values - target_q_values).detach().cpu().numpy()

        # Weighted loss (importance sampling)
        loss = (weights * F.mse_loss(current_q_values, target_q_values, reduction='none')).mean()

        # Optimize
        self.optimizer.zero_grad()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(self.policy_net.parameters(), 1.0)
        self.optimizer.step()

        # Update priorities
        self.memory.update_priorities(indices, td_errors)

        self.losses.append(loss.item())
        self.learn_step_counter += 1

        if self.learn_step_counter % self.target_update_freq == 0:
            self.target_net.load_state_dict(self.policy_net.state_dict())

        self.epsilon = max(self.epsilon_end, self.epsilon * self.epsilon_decay)
        self.clear_episode()


def train_dqn_agent(num_episodes: int = 1000, print_every: int = 50):
    """Example training function for DQN agent."""
    from main import RLTrainer

    print("\n" + "=" * 60)
    print("Training DQN Agent")
    print("=" * 60)

    agent = DQNAgent(
        name="DQN Agent",
        learning_rate=0.0005,
        gamma=0.95,
        epsilon_start=1.0,
        epsilon_end=0.01,
        epsilon_decay=0.995,
        memory_size=10000,
        batch_size=64,
        target_update_freq=10
    )

    trainer = RLTrainer(agent)
    trainer.train(num_episodes=num_episodes, print_every=print_every)

    return agent


def train_double_dqn_agent(num_episodes: int = 1000, print_every: int = 50):
    """Example training function for Double DQN agent."""
    from main import RLTrainer

    print("\n" + "=" * 60)
    print("Training Double DQN Agent")
    print("=" * 60)

    agent = DoubleDQNAgent(
        name="Double DQN",
        learning_rate=0.0005,
        gamma=0.95,
        epsilon_start=1.0,
        epsilon_end=0.01,
        epsilon_decay=0.995
    )

    trainer = RLTrainer(agent)
    trainer.train(num_episodes=num_episodes, print_every=print_every)

    return agent


def train_reinforce_agent(num_episodes: int = 1000, print_every: int = 50):
    """Example training function for REINFORCE agent."""
    from main import RLTrainer

    print("\n" + "=" * 60)
    print("Training REINFORCE Agent")
    print("=" * 60)

    agent = REINFORCEAgent(
        name="REINFORCE",
        learning_rate=0.0005,
        gamma=0.99
    )

    trainer = RLTrainer(agent)
    trainer.train(num_episodes=num_episodes, print_every=print_every)

    return agent


def train_a2c_agent(num_episodes: int = 1000, print_every: int = 50):
    """Example training function for A2C agent."""
    from main import RLTrainer

    print("\n" + "=" * 60)
    print("Training A2C Agent")
    print("=" * 60)

    agent = A2CAgent(
        name="A2C",
        learning_rate=0.0005,
        gamma=0.99,
        value_coef=0.5,
        entropy_coef=0.01
    )

    trainer = RLTrainer(agent)
    trainer.train(num_episodes=num_episodes, print_every=print_every)

    return agent


def compare_agents():
    """Compare different RL agents."""
    from main import run_headless

    agents = [
        DQNAgent(name="DQN"),
        DoubleDQNAgent(name="Double DQN"),
        DuelingDQNAgent(name="Dueling DQN"),
        REINFORCEAgent(name="REINFORCE"),
        A2CAgent(name="A2C")
    ]

    print("\n" + "=" * 60)
    print("Comparing RL Agents (Untrained)")
    print("=" * 60 + "\n")

    for agent in agents:
        print(f"\nTesting {agent.name}...")
        agent.set_training_mode(False)
        run_headless(agent, 10, 20, 10)


if __name__ == "__main__":
    # Example: Train and test a DQN agent
    print("Training DQN Agent for Tetris")
    agent = train_dqn_agent(num_episodes=500, print_every=25)

    print("\n" + "=" * 60)
    print("Testing Trained Agent")
    print("=" * 60)

    from main import run_headless

    agent.set_training_mode(False)
    run_headless(agent, 10, 20, 20)