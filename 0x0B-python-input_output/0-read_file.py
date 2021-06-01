#!/usr/bin/python3
"""contains read_file"""


def read_file(filename=""):
    """reads the contents of a file"""
    with open(filename, "r") as f:
        print(f.read())
