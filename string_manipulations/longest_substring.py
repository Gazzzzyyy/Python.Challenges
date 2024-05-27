"""
Given a string s, find the length of the longest substring without repeating characters.
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""

from typing import AnyStr


def brute_force_longest_substring(full_string: AnyStr):
    """
    O(n^2)
    """

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


def sliding_window_technique_longest_substring(full_string: AnyStr):
    """
    Finds the length of the longest substring without repeating characters.

    Args:
    s (str): The input string.

    Returns:
    int: The length of the longest substring without repeating characters.
    """
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(full_string)):
        while full_string[right] in char_set:
            char_set.remove(full_string[left])
            left += 1
        char_set.add(full_string[right])
        max_length = max(max_length, right - left + 1)

    return max_length


if __name__ == "__main__":
    # print(brute_force_longest_substring(full_string="abcabcbb"))
    print(sliding_window_technique_longest_substring(full_string="abcabcbb"))
