#!/usr/bin/python3
"""function for checking object's instance"""


def is_same_class(obj, a_class):
    """checking object's instance and returns either true or false
        Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to
    """
    if type(obj) == a_class:
        return True
    else:
        return False
