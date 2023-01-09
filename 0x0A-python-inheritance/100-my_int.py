#!/usr/bin/python3
"""
Contains the class MyInt.
"""


class MyInt(int):
    """A class that inherits from class int
    MyInt is a rebel. MyInt has == and != operators inverted.
    """
    def __eq__(self, other):
        """Method that returns != check."""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Method that returns == check."""
        return int.__eq__(self, other)
