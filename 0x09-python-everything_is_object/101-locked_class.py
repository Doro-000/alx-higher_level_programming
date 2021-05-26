#!/usr/bin/python3
"""class to demo a class that blocks dynamic attribute creation"""


class LockedClass():
    """Demo Class"""
    __slots__ = ['first_name']
