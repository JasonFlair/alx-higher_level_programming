#!/usr/bin/python3
"""Defines an class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""

    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value

    def area(self):
        """empty area function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer_validator, checks if value is an int
        :param name: name of value
        :param value: value to be checked
        :return: exception if value is not an int
        """
        self.name = name
        self.value = value

        if type(value) != int:
            raise TypeError(f"{self.name} must be an integer")
        if value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
