#!/usr/bin/env python3
import argparse
import sys
from board import TetrisBoard
from players import RandomAgent, GreedyAgent, HeuristicRLAgent
from human_player import HumanPlayer
from gui import TetrisGUI
from simple_neural_network import SimpleNNAgent
from advanced_rl_agents import (
    DQNAgent, DoubleDQNAgent, DuelingDQNAgent,
    REINFORCEAgent, A2CAgent, PrioritizedDQNAgent
)


def create_agent(agent_type: str):
    """Create agent based on type."""
    agents = {
        'human': lambda: HumanPlayer("Human"),
        'random': lambda: RandomAgent("Random AI"),
        'greedy': lambda: GreedyAgent("Greedy AI"),
        'heuristic': lambda: HeuristicRLAgent("Heuristic RL"),
        'simplenn': lambda: SimpleNNAgent("Simple NN"),#, pretrained = True),
        'dqn': lambda: DQNAgent("DQN"),
        'double_dqn': lambda: DoubleDQNAgent("Double DQN"),
        'dueling_dqn': lambda: DuelingDQNAgent("Dueling DQN"),
        'reinforce': lambda: REINFORCEAgent("REINFORCE"),
        'a2c': lambda: A2CAgent("A2C"),
        'prioritized_dqn': lambda: PrioritizedDQNAgent("Prioritized DQN"),
    }

    if agent_type not in agents:
        raise ValueError(f"Unknown agent type: {agent_type}")

    return agents[agent_type]()


def main():
    parser = argparse.ArgumentParser(description="Simplified Tetris for RL")
    parser.add_argument(
        '--agent',
        choices=['human', 'random', 'greedy', 'heuristic', 'simplenn', 'dqn', 'double_dqn', 'dueling_dqn', 'reinforce', 'a2c', 'prioritized_dqn'],
        default='human',
        help="Type of agent to use"
    )
    parser.add_argument(
        '--width',
        type=int,
        default=10,
        help="Board width (default: 10)"
    )
    parser.add_argument(
        '--height',
        type=int,
        default=20,
        help="Board height (default: 20)"
    )
    parser.add_argument(
        '--no-gui',
        action='store_true',
        help="Run without GUI (for training)"
    )
    parser.add_argument(
        '--games',
        type=int,
        default=1,
        help="Number of games to play (no-gui mode)"
    )

    args = parser.parse_args()

    try:
        # Create agent
        agent = create_agent(args.agent)
        print(f"Created agent: {agent.name}")

        if args.no_gui:
            run_headless(agent, args.width, args.height, args.games)
        else:
            run_with_gui(agent, args.width, args.height)

    except KeyboardInterrupt:
        print("\nInterrupted by user")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


def run_with_gui(agent, board_width: int, board_height: int):
    """Run game with GUI."""
    print("\n=== Tetris RL ===")
    print(f"Agent: {agent.name}")
    print("\nControls:")

    if isinstance(agent, HumanPlayer):
        print("  LEFT/RIGHT ARROWS: Select column")
        print("  R: Change rotation")
        print("  SPACE: Place piece")
        print("  Number keys 1-9,0: Jump to column")

    print("  P: Pause")
    print("  ESC: Quit")
    print("  R (when game over): Restart")
    print("\n" + "=" * 40 + "\n")

    # Create game
    board = TetrisBoard(board_width, board_height, agent)
    gui = TetrisGUI()

    # Run game loop
    gui.run(board)

    # Final stats
    stats = agent.get_stats()
    print(f"\n=== Final Statistics ===")
    print(f"Agent: {agent.name}")
    print(f"Games Played: {stats['games_played']}")
    print(f"Best Score: {stats['best_score']}")
    print(f"Average Score: {stats['average_score']:.1f}")


def run_headless(agent, board_width: int, board_height: int, num_games: int):
    """Run game without GUI - training and testing purposes"""
    print(f"\n=== Running {num_games} game(s) headless ===")
    print(f"Agent: {agent.name}")
    print(f"Board: {board_width}x{board_height}")
    print("=" * 40 + "\n")

    all_scores = []
    all_lines = []

    for game_num in range(num_games):
        board = TetrisBoard(board_width, board_height, agent)
        moves = 0
        max_moves = 10000  # Prevent infinite games

        print(f"Game {game_num + 1}/{num_games}: ", end="", flush=True)

        while not board.game_over and moves < max_moves:
            # Get action from agent
            state = board.get_state()
            action = agent.choose_action(state)

            # Execute action
            board.place_piece(action[0], action[1])
            moves += 1

            # Progress indicator
            if moves % 50 == 0:
                print(".", end="", flush=True)

        # Game ended
        final_score = board.score
        lines_cleared = board.lines_cleared

        all_scores.append(final_score)
        all_lines.append(lines_cleared)

        agent.game_ended(final_score, lines_cleared)

        print(f" Score: {final_score:>6} | Lines: {lines_cleared:>3} | Moves: {moves:>4}")

    # Summary statistics
    if num_games > 1:
        print("\n" + "=" * 40)
        print("=== SUMMARY STATISTICS ===")
        print("=" * 40)
        print(f"Agent: {agent.name}")
        print(f"Games Played: {num_games}")
        print(f"\nScores:")
        print(f"  Average: {sum(all_scores) / len(all_scores):.1f}")
        print(f"  Best: {max(all_scores)}")
        print(f"  Worst: {min(all_scores)}")
        print(f"\nLines Cleared:")
        print(f"  Average: {sum(all_lines) / len(all_lines):.1f}")
        print(f"  Best: {max(all_lines)}")
        print(f"  Worst: {min(all_lines)}")
        print("=" * 40 + "\n")


class RLTrainer:
    """
    Example training class for RL agents.
    Shows how to structure training loops.
    """

    def __init__(self, agent, board_width: int = 10, board_height: int = 20):
        self.agent = agent
        self.board_width = board_width
        self.board_height = board_height
        self.episode_count = 0

    def train_episode(self) -> dict:
        """
        Train for one episode.

        Returns:
            Episode statistics
        """
        board = TetrisBoard(self.board_width, self.board_height, self.agent)
        self.agent.set_training_mode(True)
        self.agent.clear_episode()

        episode_reward = 0
        moves = 0
        # load initial (empty board) state into prev_state
        new_state = None
        prev_state = board.get_state()
        prev_state_vector = board.get_state_vector()

        while not board.game_over and moves < 5000:
            # Get current state
            state = board.get_state()
            state_vector = board.get_state_vector()

            # Choose action
            action = self.agent.choose_action(state)

            # Execute action
            board.place_piece(action[0], action[1])


            # Calculate reward
            new_state = board.get_state()
            reward = self.agent.calculate_reward(prev_state, new_state, board.game_over)
            episode_reward += reward

            # Store experience
            self.agent.remember(prev_state_vector, action, reward)

            prev_state = new_state
            prev_state_vector = state_vector
            moves += 1

        # Train the agent
        self.agent.train()

        # Update statistics
        self.agent.game_ended(board.score, board.lines_cleared)
        self.episode_count += 1

        return {
            'episode': self.episode_count,
            'score': board.score,
            'lines': board.lines_cleared,
            'moves': moves,
            'reward': episode_reward
        }

    def train(self, num_episodes: int, print_every: int = 10):
        """
        Train for multiple episodes.

        Args:
            num_episodes: Number of episodes to train
            print_every: Print statistics every N episodes
        """
        print(f"\n=== Training {self.agent.name} ===")
        print(f"Episodes: {num_episodes}")
        print("=" * 50 + "\n")

        for episode in range(num_episodes):
            stats = self.train_episode()

            if (episode + 1) % print_every == 0:
                agent_stats = self.agent.get_stats()
                print(f"Episode {episode + 1:>4} | "
                      f"Score: {stats['score']:>6} | "
                      f"Lines: {stats['lines']:>3} | "
                      f"Avg Score: {agent_stats['average_score']:>6.1f}")

        print("\n" + "=" * 50)
        print("=== Training Complete ===")
        final_stats = self.agent.get_stats()
        print(f"Total Episodes: {final_stats['games_played']}")
        print(f"Average Score: {final_stats['average_score']:.1f}")
        print(f"Best Score: {final_stats['best_score']}")
        print("=" * 50 + "\n")


def example_training():
    """Example of how to train an RL agent."""
    print("\n=== Example: Training Heuristic RL Agent ===\n")

    # Create agent
    agent = HeuristicRLAgent("Heuristic RL")

    # Create trainer
    trainer = RLTrainer(agent)

    # Train
    trainer.train(num_episodes=100, print_every=10)

    # Test trained agent
    print("\n=== Testing Trained Agent ===\n")
    agent.set_training_mode(False)
    run_headless(agent, 10, 20, 10)

def NNTraining(num_episodes=100, print_every=10, testing_episodes=10):
    print("Training a neural network")

    agent = SimpleNNAgent(pretrained=False)
    trainer = RLTrainer(agent)
    trainer.train(num_episodes, print_every)

    print("Testing the neural network")
    agent.set_training_mode(False)
    run_headless(agent, 10, 20, testing_episodes)

    agent.save_model()


if __name__ == "__main__":
    # Uncomment to run training example
    # example_training()

    # Uncomment to train a neural network
    # NNTraining(5000, 20, 200)

    # Run normal game
    main()