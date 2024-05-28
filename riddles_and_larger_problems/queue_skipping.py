"""
It is New Year's Day and people are in line for the Wonderland rollercoaster ride.
Each person wears a sticker indicating their initial position in the queue from 1 to n .
Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker.
One person can bribe at most two others.

Determine the minimum number of bribes that took place to get to a given queue order.
Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.
"""


def minimum_bribes(q):
    """
    Determine the minimum number of bribes that took place to get to the given queue order.

    Args:
    q (list): A list of integers where each integer represents a person's initial position.

    Returns:
    None: Prints the number of bribes or 'Too chaotic' if any person has bribed more than two people.
    """
    total_bribes = 0

    # Traverse the queue
    for i in range(len(q)):
        # Check if any person has moved more than two positions ahead
        actual_position = q[i]
        expected_position = i + 1

        if actual_position - expected_position > 2:
            print("Too chaotic")
            return

        # Count the number of bribes for the current person
        for j in range(max(0, actual_position - 2), i):
            if q[j] > actual_position:
                total_bribes += 1

    print(total_bribes)


if __name__ == "__main__":

    minimum_bribes([1, 2, 3, 5, 4, 6, 7, 8])
