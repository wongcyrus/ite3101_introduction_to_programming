from typing import List


def total(numbers: List[int]) -> int:
    sum_so_far = 0
    for number in numbers:
        sum_so_far += number
    return sum_so_far


print(total([1, 2, 3]))
