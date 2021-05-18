#!/usr/bin/python3
"""Square class to represent a square"""


class Square():
    """square class with it's size and proper validation"""
    __size = None

    def __init__(self, size):
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
