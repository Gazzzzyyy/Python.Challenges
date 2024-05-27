"""
Determine if an integer array has an index where the sum of the values before the index equals the sum of the values
after the index.

example:
input [1,0,2,6,0,3]
return 3 (index of 6)
"""

from typing import List


def brute_force_find_index(array: List[int]):

    for index, value in enumerate(array):

        if index == 0:
            continue

        left, right = array[0:index], array[index + 1 :]

        if sum(left) == sum(right):
            return index

    raise IndexError("No index found")


if __name__ == "__main__":

    examples = [([1, 7, 3, 6, 5, 6], 3), ([1, 1, 1, 2, 1, 1, 1], 3), ([1, -1, 0, 0], 2)]

    for arr, expected in examples:
        result = brute_force_find_index(arr)
        print(f"Array: {arr} | Expected Index: {expected} | Calculated Index: {result}")
