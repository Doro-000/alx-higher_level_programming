#!/usr/bin/python3
"""contains Student class"""


class Student():
    """student class to represent a student"""
    def __init__(self, first_name, last_name, age):
        """instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self. age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""
        if attrs == None:
            return self.__dict__
        return {key: self.__dict__[key] for key in attrs}
