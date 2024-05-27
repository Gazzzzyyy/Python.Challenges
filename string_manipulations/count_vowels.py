"""
Write a function count_vowels that takes a string as input and returns the number of
vowels (a, e, i, o, u) in the string.
The function should be case-insensitive.
"""

from typing import AnyStr


def count_vowels(s: AnyStr) -> int:

    map = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

    for x in s.lower():

        if x in map:
            map[x] += 1

    return sum(list(map.values()))


if __name__ == "__main__":

    print(count_vowels(s="aeiou"))
    print(count_vowels(s="Gary McCormack"))
    print(count_vowels(s="yjkprt"))
    print(count_vowels(s="knkglsvnorijtj901nel lknsdwpeo oppfe"))
