#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """rectangle initialiser on init"""
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def x(self):
        """returns value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets value of x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """returns value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets value of y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """sets value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def display(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            print("")

        print('\n' * self.y, end='')
        for l in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def update(self, *args, **kwargs):
        """updates attributes of the rectangle"""
        count = 0
        for k, v in kwargs.items():
            if k == "id":
                self.id = kwargs['id']
            elif k == "height":
                self.height = kwargs['height']
            elif k == "width":
                self.width = kwargs['width']
            elif k == "x":
                self.x = kwargs['x']
            elif k == "y":
                self.y = kwargs['y']
        for arg in args:
            count += 1
        if count == 1:
            self.id = args[0]
        elif count == 2:
            self.id = args[0]
            self.width = args[1]
        elif count == 3:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
        elif count == 4:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
        elif count == 5:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]

    def to_dictionary(self):
        """returns dictionary representation"""
        return {'id': self.id, 'width': self.width, 'height': self.height, 'x': self.x, 'y': self.y}

    def __str__(self):
        """str representation of the class"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
