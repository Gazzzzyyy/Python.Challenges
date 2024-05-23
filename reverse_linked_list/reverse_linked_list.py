"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
"""

from typing import List

_Numeric = int | float | complex


def loop_backwards_reverse_list(input_list: List[_Numeric]):

    output = []

    n = len(input_list)

    for i in range(n):

        output.append(input_list[(n - 1) - i])

    print(output)


if __name__ == "__main__":
    loop_backwards_reverse_list(input_list=[1, 2, 3, 4, 5])

    loop_backwards_reverse_list(input_list=[i for i in range(-10, 21)])
