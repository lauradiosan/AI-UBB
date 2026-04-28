from abc import ABC, abstractmethod
from typing import Tuple, List, Dict, Any
import random
import numpy as np

class Agent(ABC):
    """
    Abstract base class for all Tetris agents.
    Interface: choose where to place piece.
    """

    def __init__(self, name: str = "Agent"):
        self.name = name
        self.games_played = 0
        self.total_score = 0
        self.best_score = 0
        self.total_lines = 0

    @abstractmethod
    def choose_action(self, state: Dict[str, Any]) -> Tuple[int, int]:
        """
        Choose action (column, rotation) based on game state.

        Args:
            state: Game state from board.get_state()

        Returns:
            Tuple of (column, rotation)
        """
        pass

    def game_ended(self, final_score: int, lines_cleared: int):
        """Update statistics when game ends."""
        self.games_played += 1
        self.total_score += final_score
        self.best_score = max(self.best_score, final_score)
        self.total_lines += lines_cleared

    def get_stats(self) -> Dict[str, float]:
        """Get agent statistics."""
        return {
            'games_played': self.games_played,
            'total_score': self.total_score,
            'average_score': self.total_score / max(1, self.games_played),
            'best_score': self.best_score,
            'total_lines': self.total_lines,
            'average_lines': self.total_lines / max(1, self.games_played)
        }

    def reset_stats(self):
        """Reset statistics."""
        self.games_played = 0
        self.total_score = 0
        self.best_score = 0
        self.total_lines = 0


class RandomAgent(Agent):
    """
    Random agent - chooses random valid actions.
    Good baseline for RL comparison.
    """

    def __init__(self, name: str = "Random"):
        super().__init__(name)

    def choose_action(self, state: Dict[str, Any]) -> Tuple[int, int]:
        """Choose random valid action."""
        valid_actions = state['valid_actions']
        if not valid_actions:
            return (0, 0)  # Fallback
        return random.choice(valid_actions)


class GreedyAgent(Agent):
    """
    Greedy agent using simple heuristics.
    Tries to minimize height and holes.
    """

    def __init__(self, name: str = "Greedy"):
        super().__init__(name)
        # Heuristic weights
        self.height_weight = -0.5
        self.lines_weight = 0.8
        self.holes_weight = -0.35
        self.bumpiness_weight = -0.18

    def choose_action(self, state: Dict[str, Any]) -> Tuple[int, int]:
        """Choose action using heuristic evaluation."""
        valid_actions = state['valid_actions']
        if not valid_actions:
            return (0, 0)

        best_action = None
        best_score = float('-inf')

        # Evaluate each action
        for action in valid_actions:
            score = self._evaluate_action(state, action)
            if score > best_score:
                best_score = score
                best_action = action

        return best_action if best_action else valid_actions[0]

    def _evaluate_action(self, state: Dict[str, Any], action: Tuple[int, int]) -> float:
        """Evaluate action using heuristics."""
        # Simulate action
        board_copy = state['board'].copy()
        col, rotation = action

        # Prefer middle columns
        middle_preference = 1.0 - abs(col - state['board'].shape[1] / 2) / (state['board'].shape[1] / 2)

        # Prefer lower heights in target column
        column_heights = self._get_column_heights(board_copy)
        height_penalty = -column_heights[col] if col < len(column_heights) else 0

        return middle_preference * 0.3 + height_penalty * 0.7

    def _get_column_heights(self, board: np.ndarray) -> List[int]:
        """Get height of each column."""
        heights = []
        height, width = board.shape
        for col in range(width):
            h = 0
            for row in range(height):
                if board[row, col] != 0:
                    h = height - row
                    break
            heights.append(h)
        return heights


class RLAgent(Agent):
    """
    Base class for reinforcement learning agents.
    Provides common RL functionality.
    """

    def __init__(self, name: str = "RL Agent", exploration_rate: float = 0.1):
        super().__init__(name)
        self.exploration_rate = exploration_rate
        self.training_mode = True

        # Experience storage
        self.episode_states = []
        self.episode_actions = []
        self.episode_rewards = []

    def set_training_mode(self, training: bool):
        """Set training vs evaluation mode."""
        self.training_mode = training

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
            return (0, 0)

        # Exploration
        if self.training_mode and random.random() < self.exploration_rate:
            return random.choice(valid_actions)

        # Exploitation
        return self.get_best_action(state)

    @abstractmethod
    def get_best_action(self, state: Dict[str, Any]) -> Tuple[int, int]:
        """Get best action according to learned policy."""
        pass

    def remember(self, state: np.ndarray, action: Tuple[int, int], reward: float):
        """Store experience for training."""
        if self.training_mode:
            self.episode_states.append(state)
            self.episode_actions.append(action)
            self.episode_rewards.append(reward)

    def calculate_reward(self, prev_state: Dict, new_state: Dict, game_over: bool) -> float:
        """
        Calculate reward for state transition.
        Override this for custom reward functions.

        Args:
            prev_state: Previous game state
            new_state: New game state
            game_over: Whether game ended

        Returns:
            Reward value
        """
        if game_over:
            return -10.0  # Large penalty for game over

        reward = 0.0

        # Reward for clearing lines
        lines_cleared = new_state['lines_cleared'] - prev_state['lines_cleared']
        reward += lines_cleared * lines_cleared * 5  # Exponential bonus

        # Small reward for placing pieces
        reward += 0.1

        # Penalty for increasing height
        prev_heights = self._get_max_height(prev_state['board'])
        new_heights = self._get_max_height(new_state['board'])
        reward -= max(0, new_heights - prev_heights) * 0.5

        return reward

    def _get_max_height(self, board: np.ndarray) -> int:
        """Get maximum column height."""
        height, width = board.shape
        max_h = 0
        for col in range(width):
            for row in range(height):
                if board[row, col] != 0:
                    max_h = max(max_h, height - row)
                    break
        return max_h

    def clear_episode(self):
        """Clear episode memory."""
        self.episode_states.clear()
        self.episode_actions.clear()
        self.episode_rewards.clear()

    @abstractmethod
    def train(self):
        """Train the agent using collected experience."""
        pass


class HeuristicRLAgent(RLAgent):
    """
    Example RL agent using learned weights for heuristics.
    Simple but effective baseline.
    """

    def __init__(self, name: str = "Heuristic RL"):
        super().__init__(name)
        # Learnable weights
        self.weights = {
            'height': -0.5,
            'lines': 1.0,
            'holes': -0.35,
            'bumpiness': -0.2
        }
        self.learning_rate = 0.01

    def get_best_action(self, state: Dict[str, Any]) -> Tuple[int, int]:
        """Choose action using learned heuristic weights."""
        valid_actions = state['valid_actions']
        if not valid_actions:
            return (0, 0)

        best_action = None
        best_value = float('-inf')

        for action in valid_actions:
            value = self._evaluate_action(state, action)
            if value > best_value:
                best_value = value
                best_action = action

        return best_action if best_action else valid_actions[0]

    def _evaluate_action(self, state: Dict[str, Any], action: Tuple[int, int]) -> float:
        """Evaluate action using weighted heuristics."""
        # Simple evaluation - would need full simulation for accuracy
        col, rotation = action
        board = state['board']

        # Calculate features
        heights = self._get_column_heights(board)
        avg_height = sum(heights) / len(heights)

        # Weighted evaluation
        value = 0
        value += self.weights['height'] * avg_height
        value += self.weights['lines'] * state['lines_cleared']

        return value

    def _get_column_heights(self, board: np.ndarray) -> List[int]:
        """Get column heights."""
        heights = []
        height, width = board.shape
        for col in range(width):
            h = 0
            for row in range(height):
                if board[row, col] != 0:
                    h = height - row
                    break
            heights.append(h)
        return heights

    def train(self):
        """Update weights based on episode performance."""
        if len(self.episode_rewards) == 0:
            return

        # Simple policy gradient update
        total_reward = sum(self.episode_rewards)

        # Update weights based on performance
        for key in self.weights:
            if total_reward > 0:
                self.weights[key] *= (1 + self.learning_rate)
            else:
                self.weights[key] *= (1 - self.learning_rate * 0.5)

        self.clear_episode()


class DQNAgent(RLAgent):
    """
    Deep Q-Network agent template.
    Implement with your preferred deep learning framework.
    """

    def __init__(self, name: str = "DQN", state_size: int = 200, action_size: int = 40):
        super().__init__(name)
        self.state_size = state_size
        self.action_size = action_size
        self.model = None  # Initialize your neural network here
        self.memory = []  # Experience replay buffer
        self.batch_size = 32
        self.gamma = 0.95  # Discount factor

    def get_best_action(self, state: Dict[str, Any]) -> Tuple[int, int]:
        """Get best action using Q-network."""
        valid_actions = state['valid_actions']
        if not valid_actions:
            return (0, 0)

        # Placeholder: Random choice (implement with your network)
        # In practice:
        # 1. Convert state to tensor
        # 2. Get Q-values from network
        # 3. Choose valid action with highest Q-value
        return random.choice(valid_actions)

    def train(self):
        """Train Q-network using experience replay."""
        # Placeholder for DQN training
        # Implement with PyTorch/TensorFlow:
        # 1. Sample batch from memory
        # 2. Compute target Q-values
        # 3. Update network
        pass


class PolicyGradientAgent(RLAgent):
    """
    Policy Gradient agent template.
    Implement with your preferred deep learning framework.
    """

    def __init__(self, name: str = "Policy Gradient"):
        super().__init__(name)
        self.policy_network = None  # Initialize policy network

    def get_best_action(self, state: Dict[str, Any]) -> Tuple[int, int]:
        """Sample action from policy network."""
        valid_actions = state['valid_actions']
        if not valid_actions:
            return (0, 0)

        # Placeholder: Random choice (implement with your network)
        # In practice:
        # 1. Convert state to tensor
        # 2. Get action probabilities from network
        # 3. Sample action from distribution
        return random.choice(valid_actions)

    def train(self):
        """Train policy network using REINFORCE or similar."""
        # Placeholder for policy gradient training
        pass