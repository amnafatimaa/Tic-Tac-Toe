"""
    Prints the game board to the terminal with optional result.
    
    Args:
        spots (dict): The game board's current state.
        turn (int): The current turn number.
        result (str or None): The game's result (if any).
        n (int): Board size (n x n).
"""
def new_board(spots, turn, result=None, n=3,      show_guide=False):
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
    """Return 'X' if turn is odd, 'O' if even."""
    return 'X' if turn % 2 == 1 else 'O'

def get_user_choice(current_player, total_spots):
    while True:
        choice = input(f"\nPlayer {current_player}, choose a spot (1–{total_spots}) or 'q' to quit: ").strip()
        if choice.lower() == 'q':
            return 'q'
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= total_spots:
                return choice
        print("Invalid input. Try again.")

def default_text():
    while True:
        n_input = input("Welcome to Tic Tac Toe! Select the number of rows and columns to play in (3 or more): ")
        if not n_input.isdigit() or int(n_input) < 3:
            print("Please enter a valid number (3 or greater).")
            input("Press Enter to continue...")
            continue
        n = int(n_input)
        # Make sure TicTacToe is defined or imported before this line
        