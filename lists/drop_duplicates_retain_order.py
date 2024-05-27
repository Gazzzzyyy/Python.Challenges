"""
Write a function remove_duplicates that takes a list of integers as input and returns a new list with
duplicates removed while preserving the order of the elements.
"""

from typing import List


def remove_duplicates(l: List[int]) -> List[int]:

    out = []

    seen = set()

    for i in l:
        if i in seen:
            continue
        else:
            out.append(i)
            seen.add(i)

    return out


if __name__ == "__main__":
    print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # returns [1, 2, 3, 4, 5]
    print(remove_duplicates([4, 4, 4, 4]))  # returns [4]
    print(remove_duplicates([3, 7, 9, 2, 9, 7, 9, 7]))  # returns [2,3,7,9]
