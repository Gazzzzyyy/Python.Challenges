"""
Problem Description
Given an integer n and an integer k:

Concatenate the integer n k times to form a new number p.
Compute the super digit of p.
The super digit of a number is defined as the sum of its digits until the result has only one digit.
"""




def super_digit_brute_force(n: int, k:int = 1):

    """
    Brute force
    Not great for large n and k
    """

    number = "".join([str(n) for _ in range(k)])

    if len(str(number)) == 1:
        return n

    ints = [int(x) for x in number]

    return super_digit_brute_force(sum(ints))


def super_digit_efficient(n: int, k:int = 1):


    """
    if the sum of n is x, then the sum of n*k = k*x
    """

    number = str(n)

    if len(str(number)) == 1:
        return n

    ints = [int(x) for x in number]

    return super_digit_brute_force(sum(ints)*k)





if __name__ == "__main__":

    print(super_digit_brute_force(n = 9875, k = 4))
    print(super_digit_efficient(n=9875, k=4))