#!/usr/bin/python3
"""module containing a class to demo a class that blocks dynamic attribute creation"""


class LockedClass():
    """Demo Class"""
    __slots__ = ['first_name']
