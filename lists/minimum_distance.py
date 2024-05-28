"""
Given an array of n integers, find and print the minimum absolute difference between any two elements in the array.
example: [3 -7 0 -3 6]
result 3 (3-0 or 6-3 or -3 0)
"""

from typing import List


def brute_force_min_distance(array: List[int]):

    array.sort()  # sorting implies that the difference between i and i+1 will always be less than i and i+2

    min_value = float("inf")

    for index, el in enumerate(array[:-1]):

        min_value = min(min_value, abs(el - array[index + 1]))

    return min_value


if __name__ == "__main__":

    brute_force_min_distance(array=[3, -7, 0, -3, 6])
