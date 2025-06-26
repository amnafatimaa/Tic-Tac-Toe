from function import new_board, check_turn, check_result
import os

'''Function to reset the game state'''
def reset_game(n):
    return {i: ' ' for i in range(1, n * n + 1)}, 0, True

restart = True


# Main game loop
while restart:
    os.system('cls' if os.name == 'nt' else 'clear')
    n_input = input("Welcome to Tic Tac Toe! Select the number of rows and columns to play in (3 or more): ")
    if not n_input.isdigit() or int(n_input) < 3:
        print("Please enter a valid number (3 or greater).")
        input("Press Enter to continue...")
        continue
    n = int(n_input)
    spots, turn, playing = reset_game(n)
    while playing:
        os.system('cls' if os.name == 'nt' else 'clear')
        result = check_result(spots, n)
        new_board(spots, turn, result, n)
        
        if result:
            print("Game over!")
            continue_playing = input("Do you want to play again? (y/n): ").strip().lower()
            if continue_playing == 'y':
                break  # Restart and re-prompt for n
            else:
                print("Thanks for playing!")
                playing = False
                restart = False
                break
        
        choice = input(f"Choose a spot (1–{n*n}), 'q' to quit or 'r' to restart: ")
        
        if choice == 'q':
            playing = False
            restart = False
            continue

        if choice == 'r':
            break  # Restart and re-prompt for n

        if not choice.isdigit() or int(choice) not in spots:
            print("Invalid input. Try again.")
            input("Press Enter to continue...")
            continue

        choice = int(choice)
        # Checking if spot is already taken
        if spots[choice] in ['X', 'O']:
            print("Spot already taken. Try again.")
            input("Press Enter to continue...")
            continue

        spots[choice] = check_turn(turn)
        turn += 1
