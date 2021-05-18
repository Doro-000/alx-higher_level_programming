#!/usr/bin/python3
""" Working on oop with python """


class Square():
    """Class representing a square
    
       Attributes:
            size (int): private attribute, size of the quare
    """

    __size = None

    def __init__(self, size):
        """ initialize the class

        Args:
           size (int): size of the square
        """
        self.__size = size
