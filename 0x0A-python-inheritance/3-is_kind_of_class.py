#!/usr/bin/python3
"""contains the function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """decides if obj is an instance or subclass of a_class"""
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
