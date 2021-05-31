#!/usr/bin/python3
"""contains the function lookup"""


def lookup(obj):
    """returns the list of available attributes of obj"""
    return dir(obj)
