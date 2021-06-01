#!/usr/bin/python3
"""contains classes to represent different shapes"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class to represent squares"""
    def __init__(self, size):
        """initializer"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
