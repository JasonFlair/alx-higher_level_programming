#!/usr/bin/python3
"""create a JSON rep of a file."""
import json


def from_json_string(my_str):
    """
    function to create a python rep of a json str.
    :param my_str: object to be converted from json
    :return: python object representation
    """
    return json.loads(my_str)
