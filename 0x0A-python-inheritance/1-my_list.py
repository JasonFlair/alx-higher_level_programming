#!/usr/bin/python3

"""function for returning a sorted list"""


class MyList(list):

    def print_sorted(self):
        """returns a sorted list"""
        sorted_list = sorted(self)
        print(sorted_list)
