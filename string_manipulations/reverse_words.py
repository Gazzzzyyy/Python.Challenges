"""
Write a function reverse_words that takes a string as input and returns a new string where the words are reversed.
Words are separated by spaces. The order of the words should remain the same, but each word should be reversed.
"""

from typing import AnyStr


def reverse_words(string: AnyStr) -> AnyStr:

    words = string.split(" ")

    new_words = []

    for word in words:

        new_words.append(word[::-1])

    output = " ".join(new_words).strip()
    print(output)
    return output


if __name__ == "__main__":
    reverse_words("hello world")  # returns "olleh dlrow"
    reverse_words("HackerRank is fun")  # returns "kcaRrekcaH si nuf"
