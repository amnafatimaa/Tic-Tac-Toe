"""
    Prints the game board to the terminal with optional result.
    
    Args:
        spots (list): The game board's current state.
        rows (int): Board size (rows x rows).
        turn (int): Current turn number to determine if reference grid is shown.
"""
def new_board(spots, rows, turn):
    """
    Display the game board. Empty spots show their 1-based position number on first turn (turn=0), otherwise show blank.
    """
    for row in range(rows):
        row_str = " | ".join(
            spots[row * rows + col] if spots[row * rows + col] != " " else (str(row * rows + col + 1) if turn == 0 else " ")
            for col in range(rows)
        )
        print(" " + row_str)
        if row < rows - 1:
            print("---+" * (rows - 1) + "---")

def get_user_choice(current_player, total_spots):
    """
    Prompts player for a move or 'q' to quit.
    Returns 0-based index or 'q'.
    """
    while True:
        choice = input(f"\nPlayer {current_player}, choose a spot (1–{total_spots}) or 'q' to quit: ").strip()
        if choice.lower() == 'q':
            return 'q'
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= total_spots:
                return choice - 1  # Convert to 0-based index
        print("Invalid input. Try again.")

def display_result(result):
    """
    Display the game result.
    """
    print(f"\nResult: {result}")