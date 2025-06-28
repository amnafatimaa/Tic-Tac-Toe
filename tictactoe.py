class TicTacToe:
    def __init__(self, n=3):
        self.n = n
        self.total_spots = n * n
        self.spots = {i: ' ' for i in range(1, self.total_spots + 1)}
        self.turn = 0
        self.playing = True
        self.result = None

    
    """
    Returns the symbol ('X' or 'O') for the current turn.
    
    Args:
        turn (int): The current turn number.
    
    Returns:
        str: 'X' if even turn, 'O' if odd.
    """
    def player_turn(self):
        return 'X' if self.turn % 2 == 0 else 'O'

    def make_move(self, choice):
        if self.spots[choice] in ['X', 'O']:
            return False
        self.spots[choice] = self.player_turn()
        self.turn += 1
        self.result = self.check_result()
        return True
    
    
    """
    Checks if a player has won or if it's a draw.
    
    Args:
        spots (dict): Current state of the board.
        n (int): Size of the board.
    
    Returns:
        str or None: Win message, 'Draw!', or None.
    """
    def check_result(self):
        """
        Checks win or draw conditions.
        Returns 'X wins!', 'O wins!', 'Draw!', or None.
        """
        # Rows
        for row in range(self.n):
            start = row * self.n + 1
            line = [self.spots[start + col] for col in range(self.n)]
            if line.count(line[0]) == self.n and line[0] != " ":
                return f"{line[0]} wins!"

        # Columns
        for col in range(self.n):
            line = [self.spots[col + 1 + row * self.n] for row in range(self.n)]
            if line.count(line[0]) == self.n and line[0] != " ":
                return f"{line[0]} wins!"

        # Diagonal (top-left to bottom-right)
        line = [self.spots[1 + i * (self.n + 1)] for i in range(self.n)]
        if line.count(line[0]) == self.n and line[0] != " ":
            return f"{line[0]} wins!"

        # Diagonal (top-right to bottom-left)
        line = [self.spots[self.n + i * (self.n - 1)] for i in range(self.n)]
        if line.count(line[0]) == self.n and line[0] != " ":
            return f"{line[0]} wins!"

        # Draw
        if all(self.spots[i] != " " for i in range(1, self.n * self.n + 1)):
            return "Draw!"

        return None

    def reset_game(self, n=None):
        """Resets the board and game state for a new round."""
        if n:
            self.n = n
            self.total_spots = n * n
            self.spots = {i: ' ' for i in range(1, self.total_spots + 1)}
            self.turn = 0
            self.result = None
            self.playing = True