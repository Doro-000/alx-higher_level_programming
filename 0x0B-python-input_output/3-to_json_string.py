#!/usr/bin/python3
"""contains to_json_string"""
import json


def to_json_string(my_obj):
        """returns JSON representation of an object"""
        return json.dumps(my_obj)
