from typing import List

# The following 3 lines of codes are for UnitTest and you don't need them for your real applications!
global shopping_list
global stock
global prices

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
        if stock[item] > 0:
            total += prices[item]
            stock[item] -= 1
    return total
