from typing import List

shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


# Write your code below!
def compute_bill(food: List[str]) -> float:
    total = 0
    for item in food:
        total += prices[item]
    return total
