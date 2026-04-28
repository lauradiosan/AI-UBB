"""
Choose column and rotation with keyboard for input method.
"""

from players import Agent
from typing import Dict, Any, Tuple, Optional
import pygame

class HumanPlayer(Agent):
    """
    Controls:
    - Number keys (1-9,0): Choose column
    - R: Cycle through rotations
    - SPACE: Place piece with current column/rotation
    - Left/Right arrows: Move column selection
    """

    def __init__(self, name: str = "Human"):
        super().__init__(name)
        self.selected_column = 0
        self.selected_rotation = 0
        self.action_ready = False
        self.last_action = None

    def choose_action(self, state: Dict[str, Any]) -> Tuple[int, int]:
        """
        Get action from human input.
        Returns the stored action when player presses SPACE.
        """
        if self.action_ready and self.last_action:
            action = self.last_action
            self.action_ready = False
            return action

        # Return current selection (won't be used until SPACE is pressed)
        return (self.selected_column, self.selected_rotation)

    def handle_keydown(self, key: int, board_width: int, num_rotations: int):
        """
        Handle keyboard input.

        Args:
            key: Pygame key code
            board_width: Width of the game board
            num_rotations: Number of rotations for current piece
        """
        # Number keys to select column (1-9, 0 for column 10)
        if pygame.K_1 <= key <= pygame.K_9:
            col = key - pygame.K_1
            if col < board_width:
                self.selected_column = col
        elif key == pygame.K_0:
            if board_width >= 10:
                self.selected_column = 9

        # Arrow keys to adjust column
        elif key == pygame.K_LEFT:
            self.selected_column = max(0, self.selected_column - 1)
        elif key == pygame.K_RIGHT:
            self.selected_column = min(board_width - 1, self.selected_column + 1)

        # R to cycle rotation
        elif key == pygame.K_r:
            self.selected_rotation = (self.selected_rotation + 1) % num_rotations

        # SPACE to confirm action
        elif key == pygame.K_SPACE:
            self.last_action = (self.selected_column, self.selected_rotation)
            self.action_ready = True

    def reset_selection(self):
        """Reset column and rotation selection."""
        self.selected_column = 0
        self.selected_rotation = 0
        self.action_ready = False

    def get_selection(self) -> Tuple[int, int]:
        """Get current column and rotation selection."""
        return (self.selected_column, self.selected_rotation)

    def is_action_ready(self) -> bool:
        """Check if player has confirmed an action."""
        return self.action_ready