"""
You are given a 2D matrix of size
n×m and an integer r. You have to rotate the matrix r times in a clockwise direction.

Example:
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
r = 1

output
13 9 5 1
14 10 6 2
15 11 7 3
16 12 8 4

"""

from typing import List, Tuple
import numpy


def brute_force_rotate_matrix(matrix: List[List[int]], r: int) -> List[List[int]]:
    """
    break the matrix into rings. Rotate each ring seperately
    """

    n = len(matrix)
    m = len(matrix[0])
    # output = [[0 for _ in range(m)] for _ in range(n)]
    output = matrix

    n_rings = min(n, m) // 2

    def _rotate_ring(
        top: List[int],
        right: List[int],
        bottom: List[int],
        left: List[int],
        rotations_remaining: int,
    ) -> Tuple[List[int], List[int], List[int], List[int]]:
        if rotations_remaining == 0:
            return top, right, bottom, left
        new_top, new_right, new_bottom, new_left = left, top, right, bottom
        rotations_remaining -= 1

        return _rotate_ring(
            new_top,
            new_right,
            new_bottom,
            new_left,
            rotations_remaining=rotations_remaining,
        )

    for ring_number in range(n_rings):
        print(ring_number)
        top = matrix[ring_number][
            ring_number : -(ring_number) if ring_number != 0 else None
        ]
        bottom = matrix[-(1 + ring_number)][
            ring_number : -(ring_number) if ring_number != 0 else None
        ]
        left = [x[ring_number] for x in matrix[ring_number + 1 : -(1 + ring_number)]]
        right = [
            x[-(1 + ring_number)] for x in matrix[ring_number + 1 : -(1 + ring_number)]
        ]
        new_top, new_right, new_bottom, new_left = _rotate_ring(
            top, right, bottom, left, rotations_remaining=r
        )

        output[ring_number][
            ring_number : -(ring_number) if ring_number != 0 else None
        ] = new_top
        output[-(1 + ring_number)][
            ring_number : -(ring_number) if ring_number != 0 else None
        ] = new_bottom

        for i in range(ring_number + 1, n - 1 - ring_number):
            output[i][ring_number] = new_left.pop()
            output[i][m - 1 - ring_number] = new_right.pop()

    print(output)


if __name__ == "__main__":

    mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

    # not working

    brute_force_rotate_matrix(matrix=mat, r=1)
