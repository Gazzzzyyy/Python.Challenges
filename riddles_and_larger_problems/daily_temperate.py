"""
You are given a list of integers representing daily temperatures. Implement a function daily_temperatures that
calculates the number of days you would have to wait until a warmer temperature.
If there is no future day for which this is possible, put 0 in that position.
"""

from typing import List


def daily_temperatures(T: List[int]) -> List[int]:
    """
    Given a list of daily temperatures T, returns a list such that, for each day in the input,
    tells you how many days you would have to wait until a warmer temperature. If there is no future day
    for which this is possible, put 0 instead.

    Parameters:
    T (List[int]): A list of integers representing daily temperatures.

    Returns:
    List[int]: A list of integers where the value at each index i is the number of days
               you have to wait until a warmer temperature. If there is no such day, the value is 0.
    """

    number_days = len(T)

    output = [0] * number_days

    for left_pointer, today_temp in enumerate(T):

        right_pointer = left_pointer + 1

        found = False

        while right_pointer < number_days and not found:

            if T[right_pointer] > today_temp:
                output[left_pointer] = right_pointer - left_pointer
                found = True

            right_pointer += 1

    return output


if __name__ == "__main__":
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [
        1,
        1,
        4,
        2,
        1,
        1,
        0,
        0,
    ]
    assert daily_temperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert daily_temperatures([30, 60, 90]) == [1, 1, 0]
