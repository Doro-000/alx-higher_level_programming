#!/usr/bin/python3
"""Documentation for a Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):

    """Square class that inherits from the Rectangle class
       which in turn inherited from the Base class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation of a Square object
        Args:
            size (int): the size of the square
            x (int): the x coordinate
            y (int): the y coordinate
            id (int): the id of the object
        """

        super().__init__(size, size, x, y, id)
