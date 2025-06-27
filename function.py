"""Functions for board rendering, player turn logic, and win/draw checking."""

def new_board(spots, turn, result=None, n=3):
    """
    Prints the game board to the terminal with optional result.
    
    Args:
        spots (dict): The game board's current state.
        turn (int): The current turn number.
        result (str or None): The game's result (if any).
        n (int): Board size (n x n).
    """
    for row in range(n):
        row_str = " | ".join(spots[row * n + col + 1] for col in range(n))
        print(" " + row_str)
        if row < n - 1:
            print("---+" * (n - 1) + "---")

    if not result:
        print(f"\nPlayer turn: {check_turn(turn)}")
    else:
        print(f"\nResult: {result}")


def check_turn(turn):
    """
    Returns the symbol ('X' or 'O') for the current turn.
    
    Args:
        turn (int): The current turn number.
    
    Returns:
        str: 'X' if even turn, 'O' if odd.
    """
    return 'X' if turn % 2 == 0 else 'O'


def check_result(spots, n):
    """
    Checks if a player has won or if it's a draw.
    
    Args:
        spots (dict): Current state of the board.
        n (int): Size of the board.
    
    Returns:
        str or None: Win message, 'Draw!', or None.
    """
    # Check rows
    for row in range(n):
        start = row * n + 1
        line = [spots[start + col] for col in range(n)]
        if line.count(line[0]) == n and line[0] != " ":
            return f"{line[0]} wins!"

    # Check columns
    for col in range(n):
        line = [spots[col + 1 + n * row] for row in range(n)]
        if line.count(line[0]) == n and line[0] != " ":
            return f"{line[0]} wins!"

    # Diagonal top-left to bottom-right
    line = [spots[1 + i * (n + 1)] for i in range(n)]
    if line.count(line[0]) == n and line[0] != " ":
        return f"{line[0]} wins!"

    # Diagonal top-right to bottom-left
    line = [spots[n + i * (n - 1)] for i in range(n)]
    if line.count(line[0]) == n and line[0] != " ":
        return f"{line[0]} wins!"

    # Check draw
    if all(spots[i] != " " for i in range(1, n * n + 1)):
        return "Draw!"

    return None
