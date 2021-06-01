#!/usr/bin/python3
"""containsclass_to_json"""
import json


def class_to_json(obj):
    return obj.__dict__
