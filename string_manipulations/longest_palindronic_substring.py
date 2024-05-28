"""
Given a string s, return the longest palindromic substring in s.

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Input: s = "cbbd"
Output: "bb"
"""

from typing import AnyStr
import numpy


def longest_palindromic_substring(full_string: AnyStr):
    max_strings = {i: [] for i in range(2, len(full_string) + 1)}

    found_strings = []

    for left in range(len(full_string)):
        right = left + 1

        while right <= len(full_string) - 1:
            max_strings[right - left + 1].append(full_string[left : right + 1])
            right += 1

    for i in range(len(full_string), 1, -1):
        for sub_string in max_strings[i]:
            if is_string_palindrome(sub_string):
                found_strings.append(sub_string)

        if len(found_strings) > 0:
            return found_strings

    raise Exception("No palindromic strings found")


def is_string_palindrome(sub_string: AnyStr):
    left_string, right_string = (
        sub_string[0 : int(numpy.floor(len(sub_string) / 2))],
        sub_string[int(numpy.ceil(len(sub_string) / 2)) :],
    )

    if left_string == right_string[::-1]:
        return True
    else:
        return False


if __name__ == "__main__":
    print(
        longest_palindromic_substring(
            full_string="abcdeffedcbaabcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcbaabcdefgfedcbaabcdefghij"
        )
    )
