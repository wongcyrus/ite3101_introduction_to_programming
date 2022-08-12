from random import randint
from typing import List

board = []

for x in range(0, 5):
    board.append(["O"] * 5)


def print_board(board_in: List[List[str]]) -> None:
    for row in board_in:
        print(" ".join(row))


def random_row(board_in: List[List[str]]) -> int:
    return randint(0, len(board_in) - 1)


def random_col(board_in: List[List[str]]) -> int:
    return randint(0, len(board_in) - 1)


random_row(board)
random_col(board)

# Add your code below!
