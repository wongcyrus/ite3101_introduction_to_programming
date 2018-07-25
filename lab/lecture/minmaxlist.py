from typing import List


def minmax_list(a_list: List[int]) -> (int, int):
    min_so_far = a_list[0]
    max_so_far = a_list[0]

    for a in a_list:

        if a < min_so_far:
            min_so_far = a

        if a > max_so_far:
            max_so_far = a

    return min_so_far, max_so_far


print(minmax_list([0, 4, -6, 9]))
