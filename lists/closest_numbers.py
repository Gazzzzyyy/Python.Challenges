"""
Given an array of distinct integers, find all pairs of elements with the minimum absolute difference between them.
If there are multiple pairs, list them in ascending order.
Example: 4 2 1 3 6 5

output:
1 2
2 3
3 4
4 5
5 6

example: -20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854


output:
-20 30
"""

from typing import List


def closest_numbers(array: List[int]):

    array.sort()

    distances = {}

    min_distance = float("inf")

    for i in range(len(array) - 1):

        el1, el2 = array[i], array[i + 1]

        left_distance = abs(el1 - el2)

        if left_distance <= min_distance:
            min_distance = left_distance

            if int(left_distance) in distances:

                distances[int(left_distance)].append((el1, el2))

            else:

                distances[int(left_distance)] = [(el1, el2)]

    return distances[min_distance]


if __name__ == "__main__":
    # Test case 1
    print("Test case 1:")
    n = 6
    arr = [4, 2, 1, 3, 6, 5]
    result = closest_numbers(arr)
    for pair in result:
        print(pair[0], pair[1])

    print("\nTest case 2:")
    # Test case 2
    n = 10
    arr = [
        -20,
        -3916237,
        -357920,
        -3620601,
        7374819,
        -7330761,
        30,
        6246457,
        -6461594,
        266854,
    ]
    result = closest_numbers(arr)
    for pair in result:
        print(pair[0], pair[1])

    print("\nTest case 3:")
    # Additional test case
    n = 7
    arr = [5, 4, 3, 2, 1, -1, -2]
    result = closest_numbers(arr)
    for pair in result:
        print(pair[0], pair[1])

    print("\nTest case 4:")
    # Additional test case with larger numbers
    n = 5
    arr = [1000000, 999999, 500000, 500001, -1000000]
    result = closest_numbers(arr)
    for pair in result:
        print(pair[0], pair[1])
