"""
Write a function most_frequent that takes a list of integers as input and returns the element that
appears most frequently. If there are multiple elements with the same highest frequency, return any one of them.
"""

from typing import List


def most_frequent_element(array: List[int]) -> int:

    mapping = {}

    for el in array:

        if el in mapping:
            mapping[el] += 1

        else:
            mapping[el] = 1

    max_el = max(list(mapping.values()))

    for k, v in mapping.items():

        if v == max_el:
            return k


if __name__ == "__main__":

    print(most_frequent_element([1, 3, 3, 3, 2, 2, 2, 2, 4, 4, 4]))  # returns 2
    print(most_frequent_element([5, 5, 5, 1, 1, 1, 2, 2]))  # returns 5 or 1
