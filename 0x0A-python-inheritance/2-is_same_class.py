"""function for checking object's instance"""


def is_same_class(obj, a_class):
    """checking object's instance and returns either true or false"""
    if type(obj) == a_class:
        return True
    else:
        return False
