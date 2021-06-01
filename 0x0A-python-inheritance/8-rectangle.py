#!/usr/bin/python3
"""contains classes to represent different shapes"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class to represent rectangles"""
    def __init__(self, width, height):
        """initializer"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
