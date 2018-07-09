from typing import List


def my_function(x: range) -> List[int]:
    result = []
    for i in range(0, len(x)):
        result.append(x[i])
    return result

# print(my_function(____))  # Add your range between the parentheses!
