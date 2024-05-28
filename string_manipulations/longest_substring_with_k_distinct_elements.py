"""
You are given a string s and an integer k. Implement a function longest_substring_with_k_distinct that finds
the length of the longest substring that contains at most k distinct characters.
"""


def longest_substring_with_k_distinct(s: str, k: int) -> int:
    """
    Given a string s and an integer k, finds the length of the longest substring that contains
    at most k distinct characters.

    Parameters:
    s (str): The input string.
    k (int): The maximum number of distinct characters allowed in the substring.

    Returns:
    int: The length of the longest substring that contains at most k distinct characters.
    """

    char_frequency = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        char = s[right]
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

        while len(char_frequency) > k:
            left_char = s[left]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            left += 1

        max_length = max(max_length, right - left + 1)
    return max_length


if __name__ == "__main__":
    assert (
        longest_substring_with_k_distinct("araaci", 2) == 4
    )  # The longest substring is "araa"
    assert (
        longest_substring_with_k_distinct("araaci", 1) == 2
    )  # The longest substring is "aa"
    assert (
        longest_substring_with_k_distinct("cbbebi", 3) == 5
    )  # The longest substring is "cbbeb" or "bbebi"
    assert (
        longest_substring_with_k_distinct("aa", 1) == 2
    )  # The longest substring is "aa"
