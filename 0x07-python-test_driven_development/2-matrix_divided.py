#!/usr/bin/python3
"""
    This module divides all the elements of a matrix using the method:
    matrix_divided
"""


def matrix_divided(matrix, div):
    """
    Returns a new matrix after dividing all the elements of matrix
    """
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(err_msg)
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(err_msg)
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError(err_msg)
    return ([list(map(lambda i: round(i / div, 2), row)) for row in matrix])


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
