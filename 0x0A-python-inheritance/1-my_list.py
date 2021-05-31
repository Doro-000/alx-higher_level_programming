#!/usr/bin/python3
"""contains MyList"""


class MyList(list):
    """custom list class"""
    def print_sorted(self):
        print(sorted(self))
