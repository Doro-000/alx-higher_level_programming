#!/usr/bin/python3
"""Module containing a dummy adder function for testing"""


def add_integer(a, b=98):
    """ adds integers
        Arguments:
                 @a: first integer
                 @b: second integer, defaults to 98 if not given
    """
    if type(a) not in [int, float] or not a:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float] or not b:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
