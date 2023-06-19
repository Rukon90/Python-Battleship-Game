from random import randint

# Create the game board
board = []
board_size = 5

for x in range(board_size):
    board.append(["O"] * board_size)

# Function to print the board
def print_board(board):
    for row in board:
        print(" ".join(row))

# Function to generate a random position for the ship
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

# Main game loop
print("Let's play Battleship!")
print_board(board)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
    print("Turn", turn + 1)

    # Get the user's guess
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    # Check if the guess is correct
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        break
    else:
        if (guess_row < 0 or guess_row >= board_size) or (guess_col < 0 or guess_col >= board_size):
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
        if turn == 3:
            print("Game Over")
    print_board(board)