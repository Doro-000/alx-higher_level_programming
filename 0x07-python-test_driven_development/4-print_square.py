#!/usr/bin/python3
"""Module containing a function that prints a square"""


def print_square(size):
    """ adds integers
        Arguments:
                 @size: size of the square
    """
    if type(size) is not itn:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    for i in range(size):
        for j in range(size):
            print("#", end="")
        if (i != size - 1):
            print()
        
