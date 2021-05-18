#!/usr/bin/python3
"""Square class to represent a square"""


class Square():
    """square class with it's size and proper validation"""
    __size = None
    __position = None

    def __init__(self, size, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if (type(value) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(value[0]) is not int) or (value[0] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(value[1]) is not int) or (value[1] < 0):
            raise TypeError("position most be a tuple of 2 positive integers")
        self.__positiion - value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if not self.size:
            print("")
        for i in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
