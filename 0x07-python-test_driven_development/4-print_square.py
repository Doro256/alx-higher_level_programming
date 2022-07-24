#!/usr/bin/python3
"""
    This module prints a square with the character # using the method:
    print_square
"""


def print_square(size):
    """
        Prints square pattern based on size

        Args:
            size (int): Height of the square

        Return:
            TypeError: if size is not int
            ValueError: if size < 0
    """


    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
