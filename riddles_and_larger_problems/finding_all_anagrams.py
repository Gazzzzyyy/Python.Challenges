"""
You are given a list of words and a string s. Write a function find_all_anagrams that returns a list of starting indices
of the substrings in s that are anagrams of any word in the given list. An anagram is a permutation of a word,
meaning that it is composed of the same letters in any order.
words = ["ab", "bc"]
s = "abcbac"

Output: [0, 1, 2, 3]
Explanation:
Substrings "ab", "bc", "cb", and "ba" are anagrams of the words in the list.
Their starting indices are 0, 1, 2, and 3 respectively.

The function should handle edge cases such as empty words list, empty string s, or no anagrams found.
You should aim to optimize the function for efficiency, considering the time complexity.

"""

from collections import Counter


def find_all_anagrams(words: list[str], s: str) -> list[int]:
    """
    Find all starting indices of substrings in s that are anagrams of any word in the given list.

    :param words: List of words to find anagrams of.
    :param s: The string to search within.
    :return: List of starting indices of substrings in s that are anagrams of any word in words.
    """
    if not words or not s:
        return []

    word_length = len(words[0])  # assume all words are same length

    output = []
    s_length = len(s)

    for i in range(s_length - word_length + 1):
        substring = s[i : i + word_length]
        if Counter(substring) in [Counter(word) for word in words]:
            output.append(i)

    return output


if __name__ == "__main__":

    def run_tests():
        """
        Runs a series of tests to verify the correctness of the find_all_anagrams function.
        """
        test_cases = [
            (["ab", "bc"], "abcbac", [0, 1, 2, 3]),
            (["abc", "def"], "abcdefabc", [0, 3, 6]),
            (["ab", "bc", "ca"], "abcabc", [0, 1, 2, 3, 4]),
            (["ab", "ba"], "abababab", [0, 1, 2, 3, 4, 5, 6]),
            (["abc"], "defghijk", []),
            ([], "abcdef", []),
            (["a"], "aaa", [0, 1, 2]),
        ]

        for i, (words, s, expected) in enumerate(test_cases, 1):
            result = find_all_anagrams(words, s)
            assert (
                result == expected
            ), f"Test case {i} failed: expected {expected}, got {result}"
            print(f"Test case {i} passed")

    run_tests()
