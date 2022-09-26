class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def __str__(self):
        """ prints this"""
        return f"[Rectangle] {self.__width}/{self.__height}"
