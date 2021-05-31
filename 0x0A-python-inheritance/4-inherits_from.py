#!/usr/bin/python3
"""contains the function inherits_from"""


def inherits_from(obj, a_class):
    """decides if obj is a subclass of a_class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
