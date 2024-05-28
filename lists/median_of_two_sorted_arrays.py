"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example: [1 3 8] [7 9]
Output 7.0
"""

from typing import List


def brute_force_method(array1: List[int], array2: List[int]):
    """
    O((m+n)log(m+n))
    """

    combined_list = array1 + array2  # O(m+n)
    combined_list.sort()  # O(log(m+n))

    even = True if len(combined_list) % 2 == 0 else False

    middle_index = (len(combined_list) - 1) // 2

    if even:
        return (
            combined_list[middle_index] + combined_list[middle_index + 1]
        ) / 2

    return combined_list[middle_index]


def binary_search_method(nums1: List[int], nums2: List[int]):
    # Ensure nums1 is the smaller array to minimize the binary search range
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    x, y = len(nums1), len(nums2)
    low, high = 0, x

    while low <= high:
        partitionX = (low + high) // 2
        partitionY = (x + y + 1) // 2 - partitionX

        maxX = float("-inf") if partitionX == 0 else nums1[partitionX - 1]
        minX = float("inf") if partitionX == x else nums1[partitionX]

        maxY = float("-inf") if partitionY == 0 else nums2[partitionY - 1]
        minY = float("inf") if partitionY == y else nums2[partitionY]

        if maxX <= minY and maxY <= minX:
            if (x + y) % 2 == 0:
                return (max(maxX, maxY) + min(minX, minY)) / 2
            else:
                return max(maxX, maxY)
        elif maxX > minY:
            high = partitionX - 1
        else:
            low = partitionX + 1

    raise ValueError("Input arrays are not sorted")


if __name__ == "__main__":

    def run_tests():
        test_cases = [
            {"nums1": [1, 3], "nums2": [2], "expected": 2.0},
            {"nums1": [1, 2], "nums2": [3, 4], "expected": 2.5},
            {"nums1": [0, 0], "nums2": [0, 0], "expected": 0.0},
            {"nums1": [], "nums2": [1], "expected": 1.0},
            {"nums1": [2], "nums2": [], "expected": 2.0},
            {"nums1": [1, 3, 8], "nums2": [7, 9], "expected": 7.0},
            {"nums1": [1, 2, 3, 4], "nums2": [5, 6, 7, 8], "expected": 4.5},
            {"nums1": [1, 3, 5, 7], "nums2": [2, 4, 6, 8], "expected": 4.5},
            {"nums1": [1, 2], "nums2": [1, 2, 3], "expected": 2.0},
            {"nums1": [3, 4], "nums2": [1, 2], "expected": 2.5},
            {"nums1": [1000000], "nums2": [1000000], "expected": 1000000.0},
            {
                "nums1": [-5, 3, 6, 12, 15],
                "nums2": [-12, -10, -6, -3, 4, 10],
                "expected": 3.0,
            },
        ]

        for i, test_case in enumerate(test_cases):
            nums1 = test_case["nums1"]
            nums2 = test_case["nums2"]
            expected = test_case["expected"]
            result = brute_force_method(nums1, nums2)
            assert (
                result == expected
            ), f"Test case {i + 1} failed: expected {expected}, got {result}"
            print(f"Test case {i + 1} passed.")

    run_tests()
