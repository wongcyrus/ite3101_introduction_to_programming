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


random_row(board)
random_col(board)

# Add your code below!
