
'''This function is for displaying the game board and check whose turn it is.'''
def new_board(spots, turn, result=None, n=3):
    for row in range(n):
        row_str = " | ".join(spots[row * n + col + 1] for col in range(n))
        print(" " + row_str)
        if row < n - 1:
            print("---+" * (n - 1) + "---")

    print(f"\nPlayer turn: {check_turn(turn)}")
    if result:
        print(f"Result: {result}")

'''This function prints the current state of the Tic Tac Toe board.
It displays the board with rows and columns, and indicates whose turn it is.
If there is a result (win or draw), it also displays that result.'''
def check_turn(turn):
    if turn % 2 == 0:
        return 'X'
    else:
        return 'O'

def check_result(spots, n):
    # Check rows for win
    for row in range(n):
        start = row * n + 1
        line = [spots[start + col] for col in range(n)]
        if line.count(line[0]) == n and line[0] != " ":
            return f"{line[0]} wins!"

    # Check columns for win
    for col in range(n):
        line = [spots[col + 1 + n * row] for row in range(n)]
        if line.count(line[0]) == n and line[0] != " ":
            return f"{line[0]} wins!"

    # Check diagonal 1 for win
    line = [spots[1 + i * (n + 1)] for i in range(n)]
    if line.count(line[0]) == n and line[0] != " ":
        return f"{line[0]} wins!"

    # Check diagonal 2 for win
    line = [spots[n + i * (n - 1)] for i in range(n)]
    if line.count(line[0]) == n and line[0] != " ":
        return f"{line[0]} wins!"

    # Check draw
    if all(spots[i] != " " for i in range(1, n * n + 1)):
        return "Draw!"
    return None
