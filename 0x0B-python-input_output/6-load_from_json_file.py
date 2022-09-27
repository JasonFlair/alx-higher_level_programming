#!/usr/bin/python3
"""create create python objects from JSON files."""
import json


def load_from_json_file(filename):
    """
    function to create python objects from JSON files.
    :param filename: json filename to be loaded
    :return: success
    """
    with open(filename, "r") as FILE:
        return json.load(FILE)
