#!/usr/bin/python3

"""
This module creates a class called Rectangle.
"""


class Rectangle:
    """A rectangle class."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize class."""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """To retrieve width."""
        return self.__width

    @width.setter
    def width(self, value):
        """To set width."""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """To retrieve height."""
        return self.__height

    @height.setter
    def height(self, value):
        """To set height."""
        if not isinstance(value, int):
            raise TypeErroe('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Returns the rectangle with the character #."""
        str = ""
        if self.__width != 0 or self.__height != 0:
            for row in range(self.__height):
                for col in range(self.__width):
                    str += '#'
                if row < self.__height - 1:
                    str += '\n'
            return str
        else:
            return ""

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        return 'Rectangle(%s, %s)' % (self.__width, self.__height)

    def __del__(self):
        """Prints a message when the rectangle is deleted"""
        type(self).number_of_instances -= 1
        print('Bye rectangle...')
