import pygame
import numpy as np
from typing import Optional
from board import TetrisBoard
from players import Agent
from human_player import HumanPlayer


class TetrisGUI:

    COLORS = {
        'background': (20, 20, 30),
        'board_bg': (40, 40, 55),
        'grid': (60, 60, 75),
        'text_primary': (255, 255, 255),
        'text_secondary': (160, 160, 180),
        'accent': (80, 180, 255),
        'success': (50, 220, 120),
        'warning': (255, 180, 50),
        'danger': (255, 80, 80),
        'shadow': (10, 10, 20),
    }

    PIECE_COLORS = {
        0: (40, 40, 55),  # Empty
        1: (0, 240, 240),  # I - Cyan
        2: (240, 240, 0),  # O - Yellow
        3: (160, 0, 240),  # T - Purple
        4: (0, 240, 0),  # S - Green
        5: (240, 0, 0),  # Z - Red
        6: (0, 0, 240),  # J - Blue
        7: (240, 160, 0),  # L - Orange
    }

    GHOST_COLOR = (100, 100, 120)
    SELECTION_COLOR = (255, 255, 100)

    def __init__(self, width: int = 900, height: int = 700):
        """Initialize the GUI."""
        pygame.init()

        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Tetris RL - Simplified")

        # Fonts
        self.font_large = pygame.font.Font(None, 56)
        self.font_medium = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 24)
        self.font_tiny = pygame.font.Font(None, 18)

        # Layout
        self.cell_size = 28
        self.board_padding = 50
        self.board_x = self.board_padding
        self.board_y = 120

        # Game state
        self.board = None
        self.clock = pygame.time.Clock()
        self.running = True
        self.paused = False
        self.fps = 60

        # Animation
        self.animation_time = 0
        self.show_placement_preview = True

    def set_board(self, board: TetrisBoard):
        """Set the game board."""
        self.board = board

    def _draw_rounded_rect(self, surface, color, rect, radius=8):
        """Draw a rounded rectangle."""
        pygame.draw.rect(surface, color, rect, border_radius=radius)

    def _draw_cell(self, x: int, y: int, color, size: int = None, border: bool = True):
        """Draw a single cell with modern styling."""
        if size is None:
            size = self.cell_size

        # Main cell
        cell_rect = pygame.Rect(x, y, size, size)
        self._draw_rounded_rect(self.screen, color, cell_rect, radius=4)

        # Highlight effect for non-empty cells
        if border and color != self.COLORS['board_bg']:
            # Top highlight
            highlight_color = tuple(min(255, c + 40) for c in color)
            highlight_rect = pygame.Rect(x + 2, y + 2, size - 4, size // 4)
            self._draw_rounded_rect(self.screen, highlight_color, highlight_rect, radius=3)

            # Bottom shadow
            shadow_color = tuple(max(0, c - 40) for c in color)
            shadow_rect = pygame.Rect(x + 2, y + size - size // 4 - 2, size - 4, size // 4)
            self._draw_rounded_rect(self.screen, shadow_color, shadow_rect, radius=3)

    def _draw_board(self):
        """Draw the main game board."""
        if not self.board:
            return

        board_width = self.board.width * self.cell_size
        board_height = self.board.height * self.cell_size

        # Board background with shadow
        shadow_rect = pygame.Rect(self.board_x + 5, self.board_y + 5,
                                  board_width + 20, board_height + 20)
        self._draw_rounded_rect(self.screen, self.COLORS['shadow'], shadow_rect)

        board_bg_rect = pygame.Rect(self.board_x - 10, self.board_y - 10,
                                    board_width + 20, board_height + 20)
        self._draw_rounded_rect(self.screen, self.COLORS['board_bg'], board_bg_rect)

        # Draw placement preview for human player
        if isinstance(self.board.agent, HumanPlayer) and self.show_placement_preview:
            self._draw_placement_preview()

        # Draw board cells
        for row in range(self.board.height):
            for col in range(self.board.width):
                cell_value = self.board.board[row, col]
                color = self.PIECE_COLORS.get(cell_value, self.COLORS['board_bg'])

                x = self.board_x + col * self.cell_size
                y = self.board_y + row * self.cell_size

                self._draw_cell(x, y, color)

        # Draw grid lines
        self._draw_grid(board_width, board_height)

        # Draw column numbers at bottom
        self._draw_column_indicators()

    def _draw_placement_preview(self):
        """Draw preview of where piece will be placed."""
        if not isinstance(self.board.agent, HumanPlayer):
            return

        col, rotation = self.board.agent.get_selection()
        piece_shape = self.board.get_piece_shape(self.board.current_piece_type, rotation)

        # Find landing row
        landing_row = self.board._get_landing_row(col, piece_shape)

        if landing_row is None or landing_row < 0:
            return

        # Draw ghost piece
        piece_height, piece_width = piece_shape.shape
        for i in range(piece_height):
            for j in range(piece_width):
                if piece_shape[i, j] == 1:
                    board_row = landing_row + i
                    board_col = col + j

                    if 0 <= board_row < self.board.height and 0 <= board_col < self.board.width:
                        x = self.board_x + board_col * self.cell_size
                        y = self.board_y + board_row * self.cell_size

                        # Draw ghost with outline
                        ghost_rect = pygame.Rect(x + 3, y + 3,
                                                 self.cell_size - 6, self.cell_size - 6)
                        pygame.draw.rect(self.screen, self.GHOST_COLOR, ghost_rect, 2)

    def _draw_grid(self, board_width: int, board_height: int):
        """Draw grid lines."""
        # Vertical lines
        for col in range(self.board.width + 1):
            x = self.board_x + col * self.cell_size
            pygame.draw.line(self.screen, self.COLORS['grid'],
                             (x, self.board_y), (x, self.board_y + board_height), 1)

        # Horizontal lines
        for row in range(self.board.height + 1):
            y = self.board_y + row * self.cell_size
            pygame.draw.line(self.screen, self.COLORS['grid'],
                             (self.board_x, y), (self.board_x + board_width, y), 1)

    def _draw_column_indicators(self):
        """Draw column numbers at bottom of board."""
        for col in range(min(self.board.width, 10)):
            x = self.board_x + col * self.cell_size + self.cell_size // 2
            y = self.board_y + self.board.height * self.cell_size + 15

            text = self.font_tiny.render(str((col + 1) % 10), True, self.COLORS['text_secondary'])
            text_rect = text.get_rect(center=(x, y))
            self.screen.blit(text, text_rect)

    def _draw_current_piece(self):
        """Draw current piece preview."""
        if not self.board or not self.board.current_piece_type:
            return

        panel_x = self.board_x + self.board.width * self.cell_size + 40
        panel_y = 120
        panel_width = 180
        panel_height = 140

        # Panel background
        panel_rect = pygame.Rect(panel_x, panel_y, panel_width, panel_height)
        self._draw_rounded_rect(self.screen, self.COLORS['board_bg'], panel_rect)

        # Title
        title = self.font_medium.render("CURRENT", True, self.COLORS['accent'])
        self.screen.blit(title, (panel_x + 15, panel_y + 15))

        # Draw piece
        piece_shape = self.board.get_piece_shape(self.board.current_piece_type, 0)
        piece_color = self.PIECE_COLORS[
            list(self.board.PIECES.keys()).index(self.board.current_piece_type) + 1
            ]

        # Center the piece in panel
        mini_size = 22
        piece_height, piece_width = piece_shape.shape
        start_x = panel_x + (panel_width - piece_width * mini_size) // 2
        start_y = panel_y + 60

        for i in range(piece_height):
            for j in range(piece_width):
                if piece_shape[i, j] == 1:
                    x = start_x + j * mini_size
                    y = start_y + i * mini_size
                    self._draw_cell(x, y, piece_color, mini_size)

    def _draw_next_piece(self):
        """Draw next piece preview."""
        if not self.board or not self.board.next_piece_type:
            return

        panel_x = self.board_x + self.board.width * self.cell_size + 40
        panel_y = 280
        panel_width = 180
        panel_height = 140

        # Panel background
        panel_rect = pygame.Rect(panel_x, panel_y, panel_width, panel_height)
        self._draw_rounded_rect(self.screen, self.COLORS['board_bg'], panel_rect)

        # Title
        title = self.font_medium.render("NEXT", True, self.COLORS['text_secondary'])
        self.screen.blit(title, (panel_x + 15, panel_y + 15))

        # Draw piece
        piece_shape = self.board.get_piece_shape(self.board.next_piece_type, 0)
        piece_color = self.PIECE_COLORS[
            list(self.board.PIECES.keys()).index(self.board.next_piece_type) + 1
            ]

        # Center the piece in panel
        mini_size = 22
        piece_height, piece_width = piece_shape.shape
        start_x = panel_x + (panel_width - piece_width * mini_size) // 2
        start_y = panel_y + 60

        for i in range(piece_height):
            for j in range(piece_width):
                if piece_shape[i, j] == 1:
                    x = start_x + j * mini_size
                    y = start_y + i * mini_size
                    self._draw_cell(x, y, piece_color, mini_size)

    def _draw_stats(self):
        """Draw game statistics."""
        if not self.board:
            return

        panel_x = self.board_x + self.board.width * self.cell_size + 40
        panel_y = 440
        panel_width = 180
        panel_height = 200

        # Panel background
        panel_rect = pygame.Rect(panel_x, panel_y, panel_width, panel_height)
        self._draw_rounded_rect(self.screen, self.COLORS['board_bg'], panel_rect)

        stats = [
            ("SCORE", f"{self.board.score:,}", self.COLORS['success']),
            ("LINES", str(self.board.lines_cleared), self.COLORS['accent']),
            ("PIECES", str(self.board.pieces_placed), self.COLORS['text_secondary']),
        ]

        y_offset = 20
        for label, value, color in stats:
            label_text = self.font_tiny.render(label, True, self.COLORS['text_secondary'])
            self.screen.blit(label_text, (panel_x + 15, panel_y + y_offset))

            value_text = self.font_medium.render(value, True, color)
            self.screen.blit(value_text, (panel_x + 15, panel_y + y_offset + 18))

            y_offset += 60

    def _draw_controls(self):
        """Draw control instructions for human players."""
        if not isinstance(self.board.agent, HumanPlayer):
            return

        panel_x = 50
        panel_y = self.board_y + self.board.height * self.cell_size + 60
        panel_width = self.board.width * self.cell_size

        controls = [
            "LEFT/RIGHT: Move column selection",
            "R: Change rotation",
            "SPACE: Place piece",
            "P: Pause | ESC: Quit"
        ]

        y_offset = 0
        for control in controls:
            text = self.font_tiny.render(control, True, self.COLORS['text_secondary'])
            self.screen.blit(text, (panel_x, panel_y + y_offset))
            y_offset += 20

    def _draw_selection_indicator(self):
        """Draw indicator showing selected column for human player."""
        if not isinstance(self.board.agent, HumanPlayer):
            return

        col, rotation = self.board.agent.get_selection()

        # Draw column indicator
        x = self.board_x + col * self.cell_size
        y = self.board_y - 20

        indicator_rect = pygame.Rect(x, y, self.cell_size, 10)
        self._draw_rounded_rect(self.screen, self.SELECTION_COLOR, indicator_rect, radius=3)

        # Draw rotation indicator
        rot_text = self.font_tiny.render(f"Rotation: {rotation}", True, self.COLORS['accent'])
        self.screen.blit(rot_text, (self.board_x, self.board_y - 40))

    def _draw_agent_info(self):
        """Draw agent information."""
        if isinstance(self.board.agent, HumanPlayer):
            return

        panel_x = 50
        panel_y = self.board_y + self.board.height * self.cell_size + 60
        panel_width = self.board.width * self.cell_size

        # Agent name
        name_text = self.font_small.render(f"Agent: {self.board.agent.name}",
                                           True, self.COLORS['accent'])
        self.screen.blit(name_text, (panel_x, panel_y))

        # Stats
        stats = self.board.agent.get_stats()
        y_offset = 30

        stat_lines = [
            f"Games: {stats['games_played']}",
            f"Avg Score: {stats['average_score']:.1f}",
            f"Best: {stats['best_score']}",
        ]

        for line in stat_lines:
            text = self.font_tiny.render(line, True, self.COLORS['text_secondary'])
            self.screen.blit(text, (panel_x, panel_y + y_offset))
            y_offset += 18

    def _draw_game_over(self):
        """Draw game over overlay."""
        if not self.board or not self.board.game_over:
            return

        # Semi-transparent overlay
        overlay = pygame.Surface((self.width, self.height))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))

        # Game over panel
        panel_width = 400
        panel_height = 250
        panel_x = (self.width - panel_width) // 2
        panel_y = (self.height - panel_height) // 2

        panel_rect = pygame.Rect(panel_x, panel_y, panel_width, panel_height)
        self._draw_rounded_rect(self.screen, self.COLORS['board_bg'], panel_rect, radius=15)

        # Title
        title = self.font_large.render("GAME OVER", True, self.COLORS['danger'])
        title_rect = title.get_rect(center=(panel_x + panel_width // 2, panel_y + 50))
        self.screen.blit(title, title_rect)

        # Stats
        score_text = self.font_medium.render(f"Score: {self.board.score:,}",
                                             True, self.COLORS['text_primary'])
        score_rect = score_text.get_rect(center=(panel_x + panel_width // 2, panel_y + 110))
        self.screen.blit(score_text, score_rect)

        lines_text = self.font_small.render(f"Lines: {self.board.lines_cleared}",
                                            True, self.COLORS['text_secondary'])
        lines_rect = lines_text.get_rect(center=(panel_x + panel_width // 2, panel_y + 145))
        self.screen.blit(lines_text, lines_rect)

        # Instructions
        restart_text = self.font_tiny.render("Press R to restart or ESC to quit",
                                             True, self.COLORS['text_secondary'])
        restart_rect = restart_text.get_rect(center=(panel_x + panel_width // 2, panel_y + 200))
        self.screen.blit(restart_text, restart_rect)

    def _draw_pause_overlay(self):
        if not self.paused:
            return

        overlay = pygame.Surface((self.width, self.height))
        overlay.set_alpha(150)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))

        pause_text = self.font_large.render("PAUSED", True, self.COLORS['accent'])
        pause_rect = pause_text.get_rect(center=(self.width // 2, self.height // 2))
        self.screen.blit(pause_text, pause_rect)

        instruction = self.font_small.render("Press P to resume", True, self.COLORS['text_secondary'])
        instruction_rect = instruction.get_rect(center=(self.width // 2, self.height // 2 + 50))
        self.screen.blit(instruction, instruction_rect)

    def handle_events(self):
        """Handle pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                # Global controls
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_p:
                    self.paused = not self.paused
                elif event.key == pygame.K_r and self.board and self.board.game_over:
                    self.board.reset()
                    if isinstance(self.board.agent, HumanPlayer):
                        self.board.agent.reset_selection()

                # Human player controls
                elif isinstance(self.board.agent, HumanPlayer) and not self.board.game_over:
                    num_rotations = len(self.board.PIECES[self.board.current_piece_type])
                    self.board.agent.handle_keydown(event.key, self.board.width, num_rotations)

    def update(self):
        """Update game state."""
        if not self.board or self.paused or self.board.game_over:
            return

        # Get action from agent
        state = self.board.get_state()

        # For human player, only execute when action is ready
        if isinstance(self.board.agent, HumanPlayer):
            if self.board.agent.is_action_ready():
                action = self.board.agent.choose_action(state)
                self.board.place_piece(action[0], action[1])
                self.board.agent.reset_selection()
        else:
            # AI agent - execute immediately
            action = self.board.agent.choose_action(state)
            self.board.place_piece(action[0], action[1])
            pygame.time.delay(50)  # Small delay to see AI moves

    def draw(self):
        # Clear screen
        self.screen.fill(self.COLORS['background'])

        # Title
        title = self.font_large.render("TETRIS RL", True, self.COLORS['accent'])
        title_rect = title.get_rect(center=(self.width // 2, 40))
        self.screen.blit(title, title_rect)

        # FPS counter
        fps_text = self.font_tiny.render(f"FPS: {self.clock.get_fps():.0f}",
                                         True, self.COLORS['text_secondary'])
        self.screen.blit(fps_text, (self.width - 80, 10))

        # Game elements
        self._draw_board()
        self._draw_current_piece()
        self._draw_next_piece()
        self._draw_stats()
        self._draw_selection_indicator()
        self._draw_controls()
        self._draw_agent_info()

        # Overlays
        self._draw_game_over()
        self._draw_pause_overlay()

        # Update display
        pygame.display.flip()

    def run(self, board: TetrisBoard):
        """
        Run the main game loop.

        Args:
            board: TetrisBoard instance
        """
        self.set_board(board)

        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)

        pygame.quit()

    def quit(self):
        self.running = False