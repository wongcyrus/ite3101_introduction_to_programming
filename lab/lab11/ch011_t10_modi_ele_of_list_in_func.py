from typing import List


def list_function(x: List[int]) -> int:
    return x[1]


n = [3, 5, 7]
print(list_function(n))
