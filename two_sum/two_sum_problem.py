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
import numpy

def brute_force_two_sum(array: List[int], target: int):

    output = []

    for i, num in enumerate(array):

        for j, other_num in enumerate(array):

            if i == j:
                continue

            if num + other_num == target:
                output = [i,j]
                break


        if output:
            return output

    raise ValueError("No valid outputs found")





if __name__ == "__main__":

    output = brute_force_two_sum(array=[2,7,11,15], target=9)
    assert(output == [0,1])