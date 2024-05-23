"""
Given a string s, find the length of the longest substring without repeating characters.
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""

from typing import AnyStr


def brute_force_longest_substring(full_string: AnyStr):

    final_max_length = 0

    for i, string_element in enumerate(full_string):
        this_starting_point_string = string_element

        if i == len(full_string) - 1:
            continue

        for next_string in full_string[i + 1 :]:

            if next_string not in this_starting_point_string:
                this_starting_point_string += next_string
            else:
                final_max_length = max(
                    final_max_length, len(this_starting_point_string)
                )
                break

    return final_max_length


if __name__ == "__main__":
    print(brute_force_longest_substring(full_string="abcabcbb"))
