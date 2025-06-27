import os
from function import new_board, check_turn, check_result

class TicTacToe:
    """
    A terminal-based Tic Tac Toe game that supports any board size (3x3 and up).
    """

    def __init__(self, n=3):
        self.n = n
        self.total_spots = n * n
        self.spots = {i: ' ' for i in range(1, self.total_spots + 1)}
        self.turn = 0
        self.playing = True
        self.result = None

    def reset_game(self, n=None):
        """Resets the board and game state for a new round."""
        if n:
            self.n = n
            self.total_spots = self.n * self.n
        self.spots = {i: ' ' for i in range(1, self.total_spots + 1)}
        self.turn = 0
        self.playing = True
        self.result = None

    def play(self):
        """Main game loop for playing the game."""
        while self.playing:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.result = check_result(self.spots, self.n)

            # Show guide grid before first move
            show_guide = (self.turn == 0)
            new_board(self.spots, self.turn, self.result, self.n, show_guide=show_guide)

            if self.result:
                print("Game over!")
                again = input("Do you want to play again? (y/n): ").strip().lower()
                if again == 'y':
                    self.reset_game()
                    continue
                else:
                    print("Thanks for playing!")
                    break

            choice = input(f"Choose a spot (1–{self.total_spots}), or 'q' to quit: ").strip()

            if choice == 'q':
                self.playing = False
                break

            if not choice.isdigit() or int(choice) not in self.spots:
                print("Invalid input. Try again.")
                input("Press Enter to continue...")
                continue

            choice = int(choice)

            if self.spots[choice] in ['X', 'O']:
                print("Spot already taken. Try again.")
                input("Press Enter to continue...")
                continue

            self.spots[choice] = check_turn(self.turn)
            self.turn += 1


if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        n_input = input("Welcome to Tic Tac Toe! Select the number of rows and columns to play in (3 or more): ")
        if not n_input.isdigit() or int(n_input) < 3:
            print("Please enter a valid number (3 or greater).")
            input("Press Enter to continue...")
            continue
        n = int(n_input)
        game = TicTacToe(n)
        game.play()
        break
