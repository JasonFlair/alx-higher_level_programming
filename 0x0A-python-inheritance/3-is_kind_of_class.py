#!/usr/bin/python3
"""function for checking object's instance"""


def is_kind_of_class(obj, a_class):
    """
    checks if obj is an instance of class and object
    :param obj: object to be checked
    :param a_class: class to be checked
    :return: either true or false
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
