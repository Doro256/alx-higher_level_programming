#!/usr/bin/python3
""" A Base class module """


from os import path
class Base:
    """ A Base class """
    __nb_objects = 0
    
    def __init__(self, id=None):
        """ Initialize Base class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
