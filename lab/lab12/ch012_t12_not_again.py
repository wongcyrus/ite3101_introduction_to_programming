from random import randint
from typing import List

board = []

for x in range(0, 5):
    board.append(["O"] * 5)


def print_board(board: List[List[str]]):
    for row in board:
        print(" ".join(row))


def random_row(board: List[List[str]]):
    return randint(0, len(board) - 1)


def random_col(board: List[List[str]]):
    return randint(0, len(board) - 1)


ship_row = random_row(board)
ship_col = random_col(board)

print(ship_row)
print(ship_col)

guess_row = int(input("Guess Row: "))
guess_col = int(input("Guess Col: "))

# Write your code below!
if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! You sank my battleship!")
else:
    if guess_row not in range(5) or guess_col not in range(5):
        print("Oops, that's not even in the ocean.")
    else:
        print("You missed my battleship!")
        board[guess_row][guess_col] = "X"
        print_board(board)
