from typing import List

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


def grades_sum(scores: List[float]) -> float:
    sum = 0
    for item in scores:
        sum += item
    return sum


print(grades_sum(grades))
