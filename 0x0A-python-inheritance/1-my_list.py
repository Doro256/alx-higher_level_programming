#!/usr/bin/python3
""" A module for MyList class """


class MyList(list):
    """ class MyList that inherits from list """

    def print_sorted(self):
        """ Method that that prints the list, but sorted (ascending sort) """
        print(sorted(self))
    
