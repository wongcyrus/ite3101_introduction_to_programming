from typing import List

# The following 3 lines of codes are for UnitTest and you don't need them for your real applications!
global grades
global grades_sum
global grades_average

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


def grades_sum(scores: List[float]) -> float:
    sum = 0
    for item in scores:
        sum += item
    return sum


print(grades_sum(grades))
