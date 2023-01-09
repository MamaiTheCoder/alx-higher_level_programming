#!/usr/bin/python3
"""
Contains the class BaseGeometry.
"""


class BaseGeometry():
    """A class with public instant methods."""
    def area(self):
        """Public instance method raises an Exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is an integer greater than 0."""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
