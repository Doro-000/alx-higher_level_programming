#!/usr/bin/python3
"""contains write_file"""


def write_file(filename="", text=""):
    """wrties text to a file"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
