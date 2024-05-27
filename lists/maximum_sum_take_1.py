"""
Given an array of integers arr, you can remove one element from the array to maximize the sum of the remaining elements.
Return the maximum possible sum of the remaining elements.


Input: arr = [1, -2, 0, 3]
Output: 4
Explanation: Remove the -2, then the maximum sum is 1 + 0 + 3 = 4.

Input: arr = [1, -2, -2, 3]
Output: 2
Explanation: Remove one of the -2's, then the maximum sum is 1 + -2 + 3 = 2 or 1 + -2 + 3 = 2.
"""

from typing import List


def remove_1_for_max(arr: List[int]):
    arr.pop(arr.index(min(arr)))
    return sum(arr)


if __name__ == "__main__":
    print(remove_1_for_max([1, -2, 0, 3]))
    print(remove_1_for_max([1, -2, -2, 3]))
