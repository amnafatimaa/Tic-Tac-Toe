import os
import subprocess
from tictactoe import TicTacToe
from UI import new_board, get_user_choice, display_result
import constants

def clear_screen():
    """Clear the terminal screen in a cross-platform way."""
    try:
        subprocess.run(['cls' if os.name == 'nt' else 'clear'], shell=True, check=True)
    except subprocess.CalledProcessError:
        print("\n" * 10)  # Fallback: print newlines if clear fails

def main():
    print("Welcome to Terminal Tic Tac Toe!")
    while True:
        # Get and validate board size
        try:
            rows_input = input("Enter board size (3 or more, or 'q' to quit): ")
            if rows_input.lower() == 'q':
                print("Game quit.")
                return
            if not rows_input.isdigit():
                print("Invalid input. Please enter a number.")
                continue
            rows = int(rows_input)
            if not (3 <= rows):
                print("Board size must be greater than or equal to 3.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # Initialize game
        try:
            game = TicTacToe(rows=rows)
        except Exception as e:
            print(f"Error initializing game: {e}")
            return

        # Main game loop
        while game.playing:
            clear_screen()
            new_board(game.spots, game.rows, game.turn)
            player = constants.Player_x if game.turn % 2 == 0 else constants.Player_O
            print(f"Turn {game.turn + 1}: Player {player}'s turn")  # Debug
            move = get_user_choice(player, game.total_spots)
            print(f"Player {player} chose move {move}")  # Debug
            if move == 'q':
                print("Game quit.")
                game.playing = False  # Ensure loop exits
                break
            move = int(move)  # Ensure integer (already 0-based from get_user_choice)
            if not (0 <= move < game.total_spots):
                print(f"Invalid move. Spot must be between 1 and {game.total_spots}. Try again.")
                input("Press Enter to continue...")
                continue
            if not game.make_move(move, player):
                print("Invalid move. Spot taken or out of range. Try again.")
                input("Press Enter to continue...")
                continue
            print(f"Move {move + 1} accepted for {player}")  # Debug
            result = game.check_result()
            if result:
                clear_screen()
                new_board(game.spots, game.rows, game.turn)
                display_result(result)
                break
            game.turn += 1

        # Ask to play again
        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()