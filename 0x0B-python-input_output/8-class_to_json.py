#!/usr/bin/python3
"""containsclass_to_json"""
import json


def class_to_json(obj):
    """returns the dictionary description of an obj"""
    return obj.__dict__
