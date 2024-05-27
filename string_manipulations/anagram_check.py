"""
Write a function are_anagrams that takes two strings as input and returns True if the strings are anagrams of
each other, and False otherwise. Anagrams are words or phrases made by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.
The function should be case-insensitive and ignore spaces.
"""

from typing import AnyStr


def are_anagrams(string1: AnyStr, string2: AnyStr) -> bool:

    string1 = sorted(string1.replace(" ", "").lower())
    string2 = sorted(string2.replace(" ", "").lower())

    if len(string1) != len(string2):
        return False

    for x, y in zip(string1, string2):

        if x != y:

            return False

    return True


if __name__ == "__main__":

    print(are_anagrams(string1="Dog God", string2="GodDog"))
    print(are_anagrams(string1="Cat God", string2="GodDog"))

    print(are_anagrams(string1="ertyu", string2="i"))
