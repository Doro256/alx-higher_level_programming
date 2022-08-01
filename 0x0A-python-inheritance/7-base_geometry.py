#!/usr/bin/python3
""" A module that defines a class BaseGeometry """


class BaseGeometry:
    """  A class based on 6-base_geometry.py """
    def area(self):
        """ A function that raises an area exception """
        raise Exception('area() is not implemented')
    
    def integer_validator(self, name, value):
        """ A function that validates value """
        if not isinstance(value, int):
            raise TypeError('<name> must be an integer')
        if value <= 0:
            raise ValueError('<name> must be greater than 0')
        
