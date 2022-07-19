#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""
    __size = None

    def __init__(self, size=0):
        """Initialize class

        Agrs:
            size (int): Size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("Size must be >= 0")
        self.__size = size
