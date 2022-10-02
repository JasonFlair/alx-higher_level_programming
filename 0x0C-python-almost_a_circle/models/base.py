#!/usr/bin/python3
import json


class Base:
    """base class"""
    import json

    __nb_objects = 0

    def __init__(self, id=None):
        """initialiser"""
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

