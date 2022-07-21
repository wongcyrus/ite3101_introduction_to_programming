from typing import List

# The following 6 lines of codes are for UnitTest and you don't need them for your real applications!
global grades
global grades_sum
global grades_average
global print_grades
global grades_variance
global grades_std_deviation

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


def print_grades(grades_input: List[float]):
    for grade in grades_input:
        print(grade)


def grades_sum(scores: List[float]) -> float:
    total = 0
    for score in scores:
        total += score
    return total


def grades_average(grades_input: List[float]) -> float:
    sum_of_grades = grades_sum(grades_input)
    average = sum_of_grades / float(len(grades_input))
    return average


def grades_variance(scores: List[float]) -> float:
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    return variance / len(scores)


def grades_std_deviation(variance: float) -> float:
    return variance ** 0.5
