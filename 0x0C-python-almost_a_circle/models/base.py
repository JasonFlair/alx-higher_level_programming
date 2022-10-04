#!/usr/bin/python3
"""Defines a base model class."""
import json


class Base:
    """base class
        Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    """
    import json

    __nb_objects = 0

    def __init__(self, id=None):
        """class initialiser when started"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json string"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to json file"""
        list_dictionary = [lst.to_dictionary() for lst in list_objs]
        filename = cls.__name__ + ".json"

        with open(filename, "w") as FILE:
            if list_objs is None:
                FILE.write("[]")
            else:
                FILE.write(Base.to_json_string(list_dictionary))
                # the return will be a file created called
                # the classname.json

    @staticmethod
    def from_json_string(json_string):
        """returns a dictionary"""
        if json_string is None or json_string == []:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            new = cls(1, 1, 1, 1, 1)
            # dummy variables created so that my
            # update module can update the instances
        elif cls.__name__ == "Square":
            new = cls(1, 1, 1, 1)
            # dummy parameters/variables
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances from a file"""
        try:
            filename = cls.__name__ + ".json"
            # filename will be the classname.json file
            # housing the dictionary of attributes
            # written to it by save to file
            with open(filename, "r") as afile:
                read_file = afile.read()

            list_dictionary = cls.from_json_string(read_file)
            # since from json string returns a dictionary

            # now it's time to return the instances using
            # the dicts
            output = [cls.create(**ld) for ld in list_dictionary]
            # used ld because there could be more than one dictionary

            return output
        except IOError or FileNotFoundError:
            return []
