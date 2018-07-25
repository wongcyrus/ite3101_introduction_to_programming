from typing import List


def min_list(a_list: List[int]) -> int:
    min_so_far = a_list[0]
    for a in a_list:
        if a < min_so_far:
            min_so_far = a
    return min_so_far


print(min_list([0, 4, -6, 9]))
