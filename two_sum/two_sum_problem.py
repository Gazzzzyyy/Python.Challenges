"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example:
    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

"""

from typing import List


def brute_force_two_sum(array: List[int], target: int):
    """
    Two for loops, complexity O(n^2)
    """
    output = []

    for i, num in enumerate(array):

        for j, other_num in enumerate(array):

            if i == j:
                continue

            if num + other_num == target:
                output = [i, j]
                break

        if output:
            return output

    raise ValueError("No valid outputs found")


def smarter_two_sum_problem(array: List[int], target: int):
    """
    Uses hashmaps. O(n)
    """

    map = {}

    for i, num in enumerate(array):

        difference = target - num

        if difference in map:

            return [map[difference], i]

        map[num] = i

    raise ValueError("No valid outputs found")


if __name__ == "__main__":

    output1 = brute_force_two_sum(array=[2, 7, 11, 15], target=9)
    output2 = smarter_two_sum_problem(array=[2, 7, 11, 15], target=9)
    assert output1 == [0, 1]
    assert output2 == [0, 1]
