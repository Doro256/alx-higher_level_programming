#!/usr/bin/python3
""" A rectangle module """


from base import Base


class Rectangle(Base):
    """ A Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize Rectangle class """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ To get width """
        return self.__width

    @property
    def height(self):
        """ To get height """
        return self.__height

    @property
    def x(self):
        """ To get x """
        return self.__x

    @property
    def y(self):
        """ To get y """
        return self.__y

    @width.setter
    def width(self, value):
        """ To set width """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """ To set height """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @x.setter
    def x(self, value):
        """ To set x """
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @y.setter
    def y(self, value):
        """ To set y """
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """ To return area of Rectangle """
        return self.__width * self.__height

    def display(self):
        """ To print to stdout the Recangle instance with # """
        for k in range(self.y):
            print()
        for i in range(self.height):
            for z in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        """ Returns Rectangle object as string """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute """
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

        if "id" in kwargs:
            self.id = kwargs["id"]
        if "width" in kwargs:
            self.width = kwargs["width"]
        if "height" in kwargs:
            self.height = kwargs["height"]
        if "x" in kwargs:
            self.x = kwargs["x"]
        if "y" in kwargs:
            self.y = kwargs["y"]

        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
