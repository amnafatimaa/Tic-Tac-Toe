import os
from tictactoe import TicTacToe
from UI import new_board, get_user_choice, default_text

def main():

    while True:
        game = TicTacToe(n=3)
        
        os.system('cls' if os.name == 'nt' else 'clear')
        new_board(game.spots, game.n, show_guide=(game.turn == 0))

        if __name__ == "__main__":
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                default_text()
                game = TicTacToe(n)
                game.play()
                break
        get_user_choice(game.player_turn(), game.total_spots)
        if game.result:
            print("\nResult:", game.result)
            again = input("Do you want to play again? (y/n): ").strip().lower()
            if again == 'y':
                game.reset()
                continue
            else:
                print("Thanks for playing!")
                break
        break



        
        
