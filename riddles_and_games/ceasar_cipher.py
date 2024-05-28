"""
Create a function that takes a string and shifts all characters by k elements
Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
Non letter characters don't change. Keeps capilization

example ert, 2
output gtv
"""

from typing import AnyStr


def cipher(string: AnyStr, k: int):

    output = []

    for s in string:

        if s.isalpha():

            start = ord("A") if s.isupper() else ord("a")

            new_char = chr(start + (ord(s) + k - start) % 26)

            print(new_char)

            output.append(new_char)

        else:
            output.append(s)

    print("".join(output))


if __name__ == "__main__":

    cipher(string="ert-RZ2", k=2)  # xpect gtv-TB2
