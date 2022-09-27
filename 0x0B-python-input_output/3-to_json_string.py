#!/usr/bin/python3
import json

"""create a JSON rep of a file."""


def to_json_string(my_obj):
    """
    function to create a JSON rep of a file.
    :param my_obj: object to be represented in json
    :return: json representation
    """
    return json.dumps(my_obj)
