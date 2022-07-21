from typing import List
# The following 7 lines of codes are for UnitTest and you don't need them for your real applications!
global lloyd
global alice
global tyler
global average
global get_average
global get_letter_grade
global get_class_average


lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}


def average(numbers: List[float]) -> float:
    total = sum(numbers)
    return total / len(numbers)


def get_average(student: dict) -> float:
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return 0.1 * homework + 0.3 * quizzes + 0.6 * tests


def get_letter_grade(score: float) -> str:
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


print(get_letter_grade(get_average(lloyd)))


# Add your function below!
def get_class_average(class_list: List[dict]) -> float:
    results = []
    for student in class_list:
        results.append(get_average(student))
    return average(results)

# Add code below!
