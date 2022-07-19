#!/usr/bin/python3

class Square:
    """A square class"""

    def __init__(self, size=0):
        """Initialize a new square.

                Args:
                    size (int): The size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("Size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area"""
        return (self.__size * self.__size)
