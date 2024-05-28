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
        return (combined_list[middle_index] + combined_list[middle_index + 1]) / 2

    return combined_list[middle_index]


def binary_search_method(array1: List[int], array2: List[int]):
    # Ensure nums1 is the smaller array
    if len(array1) > len(array2):
        nums1, nums2 = array2, array1

    m, n = len(nums1), len(nums2)
    imin, imax, half_len = 0, m, (m + n + 1) // 2

    while imin <= imax:
        # Partition nums1 at index i
        i = (imin + imax) // 2
        # Partition nums2 at index j
        j = half_len - i

        # i is too small, must increase it
        if i < m and nums1[i] < nums2[j - 1]:
            imin = i + 1
        # i is too large, must decrease it
        elif i > 0 and nums1[i - 1] > nums2[j]:
            imax = i - 1
        else:
            # i is perfect

            # Handle the edge cases where i or j is 0
            if i == 0:
                max_of_left = nums2[j - 1]
            elif j == 0:
                max_of_left = nums1[i - 1]
            else:
                max_of_left = max(nums1[i - 1], nums2[j - 1])

            # If the total length is odd, return the max of left part
            if (m + n) % 2 == 1:
                return max_of_left

            # Handle the edge cases where i or j is at the end of their respective arrays
            if i == m:
                min_of_right = nums2[j]
            elif j == n:
                min_of_right = nums1[i]
            else:
                min_of_right = min(nums1[i], nums2[j])

            # If the total length is even, return the average of the max of left part and min of right part
            return (max_of_left + min_of_right) / 2.0


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
