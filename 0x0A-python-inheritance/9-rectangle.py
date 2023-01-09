#!/usr/bin/python3
"""
Contains the class BaseGeometry and subclass Rectangle.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation of the rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Method that returns the area of the instance."""
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
