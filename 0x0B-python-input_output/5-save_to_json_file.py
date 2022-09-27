#!/usr/bin/python3
"""create a JSON file and save python objects."""
import json


def save_to_json_file(my_obj, filename):
    """
    function to create a JSON file and save python objects.
    :param my_str: object to be converted from json
    :param filename: json filename to be created
    :return: success
    """
    with open(filename, "w") as FILE:
        json.dump(my_obj, FILE)
