#!/usr/bin/python3
"""Contains Base class"""
import json


class Base:
    """base class to manage ID
    Attributes:
            id: int, Id of a Base object
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """instantiation"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """serializes a list of dicts representing shapes"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """deserializes a json list represented as a string"""
        if json_string is None or json_string == "" or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves a list of objects to a json file"""
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as f:
            f.write(cls.to_json_string([o.to_dictionary() for o in list_objs]))

    @classmethod
    def create(cls, **dictionary):
        """creates an instances with all attributes set"""
        new = cls.__new__(cls)
        new.__init__(10, 10)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """retrives a list of instances from a json file"""
        filename = "{}.json".format(cls.__name__)
        instances = []
        try:
            with open(filename, "r") as f:
                content = cls.from_json_string(f.read())
            for dict in content:
                instances.append(cls.create(**dict))
            return instances
        except FileNotFoundError:
            return instances
