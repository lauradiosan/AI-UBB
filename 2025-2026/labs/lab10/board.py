"""
Tetris Board
Action space: Choose column and rotation, piece drops instantly
"""

import random
import numpy as np
from typing import List, Tuple, Optional, Dict, Any

class TetrisBoard:

    PIECES = {
        'I': [
            [[1, 1, 1, 1]],  # Horizontal
            [[1], [1], [1], [1]]  # Vertical
        ],
        'O': [
            [[1, 1], [1, 1]]  # Square (no rotation needed)
        ],
        'T': [
            [[0, 1, 0], [1, 1, 1]],  # T pointing up
            [[1, 0], [1, 1], [1, 0]],  # T pointing right
            [[1, 1, 1], [0, 1, 0]],  # T pointing down
            [[0, 1], [1, 1], [0, 1]]   # T pointing left
        ],
        'S': [
            [[0, 1, 1], [1, 1, 0]],  # Horizontal
            [[1, 0], [1, 1], [0, 1]]  # Vertical
        ],
        'Z': [
            [[1, 1, 0], [0, 1, 1]],  # Horizontal
            [[0, 1], [1, 1], [1, 0]]  # Vertical
        ],
        'J': [
            [[1, 0, 0], [1, 1, 1]],  # J normal
            [[1, 1], [1, 0], [1, 0]],  # J rotated 90
            [[1, 1, 1], [0, 0, 1]],  # J rotated 180
            [[0, 1], [0, 1], [1, 1]]   # J rotated 270
        ],
        'L': [
            [[0, 0, 1], [1, 1, 1]],  # L normal
            [[1, 0], [1, 0], [1, 1]],  # L rotated 90
            [[1, 1, 1], [1, 0, 0]],  # L rotated 180
            [[1, 1], [0, 1], [0, 1]]   # L rotated 270
        ]
    }

    def __init__(self, width: int = 10, height: int = 20, agent=None):
        """
        Args:
            width: Board width (default: 10)
            height: Board height (default: 20)
            agent: Agent/player that will play the game
        """
        self.width = width
        self.height = height
        self.agent = agent

        # Game state
        self.board = np.zeros((height, width), dtype=np.int8)
        self.score = 0
        self.lines_cleared = 0
        self.pieces_placed = 0
        self.game_over = False

        # Current piece
        self.current_piece = None
        self.current_piece_type = None
        self.next_piece_type = None

        # Initialize
        self._spawn_new_piece()
        self._generate_next_piece()

    def _get_random_piece(self) -> str:
        return random.choice(list(self.PIECES.keys()))

    def _spawn_new_piece(self):
        if self.next_piece_type:
            self.current_piece_type = self.next_piece_type
        else:
            self.current_piece_type = self._get_random_piece()

    def _generate_next_piece(self):
        self.next_piece_type = self._get_random_piece()

    def get_piece_shape(self, piece_type: str = None, rotation: int = 0) -> np.ndarray:
        """
        Get piece shape as numpy array.
        Args:
            piece_type: Type of piece (default: current piece)
            rotation: Rotation index (default: 0)
        """
        if piece_type is None:
            piece_type = self.current_piece_type

        rotations = self.PIECES[piece_type]
        rotation = rotation % len(rotations)
        return np.array(rotations[rotation], dtype=np.int8)

    def get_valid_actions(self) -> List[Tuple[int, int]]:
        """
        Get all valid (column, rotation) actions for current piece.
        Returns:
            List of (column, rotation) tuples
        """
        if self.game_over:
            return []

        valid_actions = []
        piece_type = self.current_piece_type
        num_rotations = len(self.PIECES[piece_type])

        for rotation in range(num_rotations):
            piece_shape = self.get_piece_shape(piece_type, rotation)
            piece_width = piece_shape.shape[1]

            # Try each column
            for col in range(self.width - piece_width + 1):
                if self._can_place_piece(col, rotation):
                    valid_actions.append((col, rotation))

        return valid_actions

    def _can_place_piece(self, col: int, rotation: int) -> bool:
        """
        Check if piece can be placed at column with rotation.

        Args:
            col: Starting column
            rotation: Rotation index
        """
        piece_shape = self.get_piece_shape(self.current_piece_type, rotation)

        # Find where piece would land
        landing_row = self._get_landing_row(col, piece_shape)

        if landing_row is None:
            return False

        # Check if placement is valid
        piece_height, piece_width = piece_shape.shape

        # Check if piece goes above board
        if landing_row < 0:
            return False

        return True

    def _get_landing_row(self, col: int, piece_shape: np.ndarray) -> Optional[int]:
        """
        Get the row where piece would land if dropped at column.

        Args:
            col: Starting column
            piece_shape: Piece shape array

        Returns:
            Landing row or None if can't place
        """
        piece_height, piece_width = piece_shape.shape

        # Start from top and find where piece hits something
        for row in range(self.height):
            # Check if piece collides with board at this position
            if self._collides(row, col, piece_shape):
                # Place at previous row
                return row - 1

        # Piece lands at bottom
        return self.height - piece_height

    def _collides(self, row: int, col: int, piece_shape: np.ndarray) -> bool:
        """Check if piece collides with board at position."""
        piece_height, piece_width = piece_shape.shape

        # Check boundaries
        if row + piece_height > self.height:
            return True
        if col + piece_width > self.width:
            return True
        if col < 0 or row < 0:
            return True

        # Check collision with existing pieces
        for i in range(piece_height):
            for j in range(piece_width):
                if piece_shape[i, j] == 1:
                    board_row = row + i
                    board_col = col + j
                    if board_row >= 0 and self.board[board_row, board_col] != 0:
                        return True

        return False

    def place_piece(self, col: int, rotation: int) -> bool:
        """
        Place current piece at column with rotation.
        This is the main action method for RL agents.

        Args:
            col: Column to place piece
            rotation: Rotation index

        Returns:
            True if successful, False if invalid action
        """
        if self.game_over:
            return False

        piece_shape = self.get_piece_shape(self.current_piece_type, rotation)

        landing_row = self._get_landing_row(col, piece_shape)

        if landing_row is None or landing_row < 0:
            # Invalid placement or piece goes above board - game over
            self.game_over = True
            return False

        # Place the piece on board
        piece_height, piece_width = piece_shape.shape
        piece_value = list(self.PIECES.keys()).index(self.current_piece_type) + 1

        for i in range(piece_height):
            for j in range(piece_width):
                if piece_shape[i, j] == 1:
                    board_row = landing_row + i
                    board_col = col + j
                    if board_row >= 0:
                        self.board[board_row, board_col] = piece_value

        self.pieces_placed += 1

        # Clear completed lines
        lines_cleared = self._clear_lines()
        self._update_score(lines_cleared)

        # Spawn next piece
        self._spawn_new_piece()
        self._generate_next_piece()

        # Check if new piece can be placed anywhere
        if not self.get_valid_actions():
            self.game_over = True

        return True

    def _clear_lines(self) -> int:
        """
        Clear completed lines.

        Returns:
            Number of lines cleared
        """
        lines_to_clear = []

        for row in range(self.height):
            if np.all(self.board[row] != 0):
                lines_to_clear.append(row)

        if lines_to_clear:
            # Remove cleared lines
            self.board = np.delete(self.board, lines_to_clear, axis=0)
            # Add empty lines at top
            new_lines = np.zeros((len(lines_to_clear), self.width), dtype=np.int8)
            self.board = np.vstack([new_lines, self.board])

        cleared_count = len(lines_to_clear)
        self.lines_cleared += cleared_count
        return cleared_count

    def _update_score(self, lines_cleared: int):
        """Update score based on lines cleared."""
        if lines_cleared == 0:
            return

        # Standard Tetris scoring
        points = {1: 100, 2: 300, 3: 500, 4: 800}
        self.score += points.get(lines_cleared, lines_cleared * 100)

    def get_state(self) -> Dict[str, Any]:
        """
        Get current game state.

        Returns:
            Dictionary with game state information
        """
        return {
            'board': self.board.copy(),
            'current_piece': self.current_piece_type,
            'next_piece': self.next_piece_type,
            'score': self.score,
            'lines_cleared': self.lines_cleared,
            'pieces_placed': self.pieces_placed,
            'game_over': self.game_over,
            'valid_actions': self.get_valid_actions()
        }

    def get_state_vector(self) -> np.ndarray:
        """
        Get state as feature vector for RL agents.
        Includes board state and useful features.

        Returns:
            Numpy array with state features
        """
        features = []

        # Flatten board
        features.extend(self.board.flatten())

        # Column heights
        heights = self._get_column_heights()
        features.extend(heights)

        # Number of holes
        features.append(self._count_holes())

        # Bumpiness (height differences)
        features.append(self._calculate_bumpiness(heights))

        # Current piece encoding (one-hot)
        piece_types = list(self.PIECES.keys())
        piece_encoding = [0] * len(piece_types)
        if self.current_piece_type:
            piece_idx = piece_types.index(self.current_piece_type)
            piece_encoding[piece_idx] = 1
        features.extend(piece_encoding)

        return np.array(features, dtype=np.float32)

    def _get_column_heights(self) -> List[int]:
        """Get height of each column."""
        heights = []
        for col in range(self.width):
            height = 0
            for row in range(self.height):
                if self.board[row, col] != 0:
                    height = self.height - row
                    break
            heights.append(height)
        return heights

    def _count_holes(self) -> int:
        """Count number of holes (empty cells below filled cells)."""
        holes = 0
        for col in range(self.width):
            found_block = False
            for row in range(self.height):
                if self.board[row, col] != 0:
                    found_block = True
                elif found_block and self.board[row, col] == 0:
                    holes += 1
        return holes

    def _calculate_bumpiness(self, heights: List[int]) -> int:
        """Calculate bumpiness (sum of absolute height differences)."""
        bumpiness = 0
        for i in range(len(heights) - 1):
            bumpiness += abs(heights[i] - heights[i + 1])
        return bumpiness

    def reset(self):
        """Reset the game to initial state."""
        self.board = np.zeros((self.height, self.width), dtype=np.int8)
        self.score = 0
        self.lines_cleared = 0
        self.pieces_placed = 0
        self.game_over = False
        self._spawn_new_piece()
        self._generate_next_piece()

    def render_text(self) -> str:
        """
        Render board as text

        Returns:
            String representation of board
        """
        lines = []
        lines.append("+" + "-" * self.width + "+")

        for row in self.board:
            line = "|"
            for cell in row:
                line += "█" if cell != 0 else " "
            line += "|"
            lines.append(line)

        lines.append("+" + "-" * self.width + "+")
        lines.append(f"Score: {self.score} | Lines: {self.lines_cleared} | Pieces: {self.pieces_placed}")

        return "\n".join(lines)