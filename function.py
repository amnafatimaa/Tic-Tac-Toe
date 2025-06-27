def new_board(spots, turn, result=None, n=3, show_guide=False):
    """
    Display the game board. If show_guide is True, show cell numbers instead of X/O/blank.
    """
    for row in range(n):
        row_str = " | ".join(
            str(row * n + col + 1) if show_guide else spots[row * n + col + 1]
            for col in range(n)
        )
        print(" " + row_str)
        if row < n - 1:
            print("---+" * (n - 1) + "---")

    if result:
        print(f"\nResult: {result}")
    elif not show_guide:
        print(f"\nPlayer turn: {check_turn(turn)}")


def check_turn(turn):
    """Returns 'X' on even turns, 'O' on odd."""
    return 'X' if turn % 2 == 0 else 'O'


def check_result(spots, n):
    """
    Checks win or draw conditions.
    Returns 'X wins!', 'O wins!', 'Draw!', or None.
    """
    # Rows
    for row in range(n):
        start = row * n + 1
        line = [spots[start + col] for col in range(n)]
        if line.count(line[0]) == n and line[0] != " ":
            return f"{line[0]} wins!"

    # Columns
    for col in range(n):
        line = [spots[col + 1 + row * n] for row in range(n)]
        if line.count(line[0]) == n and line[0] != " ":
            return f"{line[0]} wins!"

    # Diagonal (top-left to bottom-right)
    line = [spots[1 + i * (n + 1)] for i in range(n)]
    if line.count(line[0]) == n and line[0] != " ":
        return f"{line[0]} wins!"

    # Diagonal (top-right to bottom-left)
    line = [spots[n + i * (n - 1)] for i in range(n)]
    if line.count(line[0]) == n and line[0] != " ":
        return f"{line[0]} wins!"

    # Draw
    if all(spots[i] != " " for i in range(1, n * n + 1)):
        return "Draw!"

    return None
