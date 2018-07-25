from typing import List


def total(numbers: List[int]) -> int:
    total_so_far = 0
    for number in numbers:
        total_so_far += number
    return total_so_far


print(total([1, 2, 3]))
print(total([7, -4, 1, 6, 0]))
print(total([]))
