"""
Two players are playing a game called Tower Breakers. The rules are as follows:

There are n towers, each of height m.
The players take turns. Player 1 always goes first.
On each player's turn, the player must choose a tower of height h and reduce its height to any number x, where 1 ≤ x < h and x divides h evenly.
If a player cannot make a move, they lose the game.
Given the number of towers n and the height of each tower m, determine which player will win if both play optimally.
"""


def can_make_move(height):

    return height > 1


def make_move(height):

    moves = []
    for i in range(1, height):
        if height % i == 0:
            moves.append(i)
    return moves


def tower_breakers_brute_force(n, m):

    # Initialize the towers
    towers = [m] * n

    # Player 1 starts
    currentPlayer = 1

    # Simulate the game
    while True:
        moveMade = False
        for i in range(n):
            if can_make_move(towers[i]):
                possibleMoves = make_move(towers[i])
                if possibleMoves:
                    # Make a move by selecting the first possible move
                    towers[i] = possibleMoves[0]
                    moveMade = True
                    break

        if not moveMade:
            # No move can be made, current player loses
            return 2 if currentPlayer == 1 else 1

        # Switch player
        currentPlayer = 2 if currentPlayer == 1 else 1


def tower_breaker(n: int, m: int) -> int:
    """

    work smarter not harder...
    """
    if m == 1:
        # player 1 can never move so always loses
        return 2

    elif n % 2 == 0:
        # player 2 can always match the moves of player 1 so can always win
        return 2

    else:
        # player 1 can always force the second player to only have a height of 1, thus player 1 wins
        return 1
