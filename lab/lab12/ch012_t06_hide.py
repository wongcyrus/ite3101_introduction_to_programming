from random import randint
from typing import List

board = []

for x in range(0, 5):
    board.append(["O"] * 5)


def print_board(board: List[List[str]]):
    for row in board:
        print(" ".join(row))

# Add your code below!
