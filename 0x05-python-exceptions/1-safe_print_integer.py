#!/usr/bin/python3

"""Print an integer with "{:d}".format().

Args:
    value (int): Integer to print.

Returns:
    False - for TypeError, ValueErro
    Otherwise True
"""


def safe_print_integer(value):
    while True:
        try:
            print("{:d}".format(value))
            return True
        except (TypeError, ValueError):
            return False
