from typing import List


def squares(limit: int) -> List[int]:
    answer = []
    for n in range(0, limit):
        answer.append(n ** 2)
    return answer


def total(numbers: List[int]) -> int:
    sum_so_far = 0
    for number in numbers:
        sum_so_far += number
    return sum_so_far
