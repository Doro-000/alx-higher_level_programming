#!/usr/bin/python3
"""contains class_to_json"""


def class_to_json(obj):
    """returns the dictionary description of an obj"""
    return obj.__dict__
