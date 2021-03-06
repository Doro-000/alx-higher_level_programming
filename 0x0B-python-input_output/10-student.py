#!/usr/bin/python3
"""contains Student class"""


class Student():
    """student class to represent a student"""
    def __init__(self, first_name, last_name, age):
        """instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""
        if type(attrs) is not list:
            return self.__dict__
        for x in attrs:
            if type(x) is not str:
                return self.__dict__
        final_dict = {}
        for key in attrs:
            if key in self.__dict__.keys():
                final_dict.update({key: self.__dict__[key]})
        return final_dict
