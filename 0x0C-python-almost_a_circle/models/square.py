#!/usr/bin/python3
""" A square module """


class Square(Rectangle):
    """ A Square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize Square class """
        super().init__(id, x, y, size, size)
        self.size = size

    @property
    def size(self):
        """ To get size """
        return self.__width

    @size.setter
    def size(self, size):
        """ To set size """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size <= 0:
            raise ValueError('size must be > 0')
        self.__width = size
        self.__height = size

    def __str__(self):
        """ Returns Square object as string """
        return "[Square] ({}) {}/{} - size".format(self.id, self.x, self.y,
                                                       self.size)
    def update(self, *args, **kwargs):
        """ Assigns argument to each attribute """
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

        if "id" in kwargs:
            self.id = kwargs["id"]
        if "size" in kwargs:
            self.size = kwargs["size"]
        if "x" in kwargs:
            self.x = kwargs["x"]
        if "y" in kwargs:
            self.y = kwargs["y"]

    def to_dictionary(self):
        """ String representation of object """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
