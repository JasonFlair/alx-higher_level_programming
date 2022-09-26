#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """a square using Rectangle."""

    def __init__(self, size):
        """initialising function"""
        self.__size = size

        self.integer_validator("size", size)

    def area(self):
        """Return the area of the square."""
        return (self.__size * self.__size)

    def __str__(self):
        """ prints this"""
        return f"[Rectangle] {self.__size}/{self.__size}"
