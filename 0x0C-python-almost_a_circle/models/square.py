#!/usr/bin/python3
from models.rectangle import Rectangle
"""contains Square class to represent squares"""


class Square(Rectangle):
    """class to represent a Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """instantiation"""
        super().__init__(size, size, x, y, id)
