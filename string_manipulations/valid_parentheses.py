"""
Write a function is_valid_parentheses that takes a string containing just the characters '(', ')', '{', '}', '[' and ']'
and determines if the input string is valid. An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""

from typing import AnyStr


def is_valid_parentheses(string: AnyStr) -> bool:

    mapping = {")": "(", "}": "{", "]": "["}

    stack = []

    for char in string:

        if char in mapping.values():

            stack.append(char)
        else:

            expected_char_to_remove = mapping[char]
            if stack and expected_char_to_remove == stack[-1]:
                stack = stack[:-1]
            else:
                return False

    if len(stack) != 0:
        return False

    return True


if __name__ == "__main__":
    print(is_valid_parentheses(")"))
    print(is_valid_parentheses("()"))  # returns True
    print(is_valid_parentheses("()[]{}"))  # returns True
    print(is_valid_parentheses("(]"))  # returns False
    print(is_valid_parentheses("([)]"))  # returns False
    print(is_valid_parentheses("{[]}"))  # returns True
