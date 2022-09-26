#!/usr/bin/python3
"""function for checking object's instance"""


def inherits_from(obj, a_class):
    """
    checks if obj is an instance of class and object
    but doesnt return true for type
    :param obj: object to be checked
    :param a_class: class to be checked
    :return: either true or false
    """
    if isinstance(obj, a_class):
        if type(obj) == a_class:
            return False
        return True
    else:
        return False
