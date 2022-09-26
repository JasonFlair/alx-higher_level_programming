#!/usr/bin/python3
"""function for returning a sorted list"""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """returns a sorted list"""
        sorted_list = sorted(self)
        print(sorted_list)
