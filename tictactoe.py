
class TicTacToe:
    def __init__(self, rows=3):
        self.rows = rows
        self.total_spots = rows * rows
        self.spots = [" " for _ in range(self.total_spots)]
        self.turn = 0
        self.playing = True
        self.result = None

    
    def make_move(self, choice, player) -> bool:
        """
        Place player's symbol on the board if the move is valid.
        Args:
        choice (int): 0-based index of the spot.
        player (str): 'X' or 'O'.
        Returns:
        bool: True if move was valid, False otherwise.
        """
        if 0 <= choice < self.total_spots and self.spots[choice] == " ":
            self.spots[choice] = player
            self.turn += 1
            self.result = self.check_result()
            return True
        return False

   
    def check_result(self) -> str | None:
        """
        Checks if a player has won or if it's a draw.

        Args:
            spots (list): Current state of the board.
            rows (int): Size of the board.

        Returns:
            str or None: Win message, 'Draw!', or None.
        """
        
        # Rows
        for row in range(self.rows):
            start = row * self.rows
            if all(self.spots[start + col] == self.spots[start] for col in range(self.rows)) and self.spots[start] != " ":
                self.playing = False
                return f"{self.spots[start]} wins!"

        # Columns
        for col in range(self.rows):
            if all(self.spots[row * self.rows + col] == self.spots[col] for row in range(self.rows)) and self.spots[col] != " ":
                self.playing = False
                return f"{self.spots[col]} wins!"

        # Diagonal (top-left to bottom-right)
        if all(self.spots[i * (self.rows + 1)] == self.spots[0] for i in range(self.rows)) and self.spots[0] != " ":
            self.playing = False
            return f"{self.spots[0]} wins!"

        # Diagonal (top-right to bottom-left)
        if all(self.spots[(i + 1) * (self.rows - 1)] == self.spots[self.rows - 1] for i in range(self.rows)) and self.spots[self.rows - 1] != " ":
            self.playing = False
            return f"{self.spots[self.rows - 1]} wins!"

        # Draw
        if all(spot != " " for spot in self.spots):
            self.playing = False
            return "Draw!"
        
        return None
    def reset_game(self, rows=None):
        """Resets the board and game state for a new round."""
        self.rows = rows if rows is not None else self.rows
        self.total_spots = self.rows * self.rows
        self.spots = [" " for _ in range(self.total_spots)]
        self.turn = 0
        self.result = None
        self.playing = True