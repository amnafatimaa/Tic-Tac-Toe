import os
from tictactoe import TicTacToe
from UI import new_board, get_user_choice, display_result

def main():
    print("Welcome to Terminal Tic Tac Toe!")
    rows_input = input("Enter number of rows (3 or more): ")
    rows = int(rows_input) if rows_input.isdigit() and int(rows_input) >= 3 else 3
    game = TicTacToe(rows=rows)

    while game.playing:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
        new_board(game.spots, game.rows, game.turn)
        player = 'X' if game.turn % 2 == 0 else 'O'
        move = get_user_choice(player, game.total_spots)
        if move == 'q':
            print("Game quit.")
            break
        if not game.make_move(move, player):
            print("Invalid move. Spot taken or out of range. Try again.")
            continue
        result = game.check_result()
        if result:
            new_board(game.spots, game.rows, game.turn)
            display_result(result)
            break

if __name__ == "__main__":
    main()