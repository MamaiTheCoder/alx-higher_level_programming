#!/usr/bin/python3
"""Square class definition"""


class Square:
    """
    Represents a square:
    Attribute:
        __size(int): size of a side of the square
    """
    def __init__(self, size):
        """
        Initializes a square
        Args:
            size (int): size of a side of the square
        Return: None
        """
        self.__size = size
