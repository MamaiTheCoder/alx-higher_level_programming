#!/usr/bin/python3
"""defines a class Square"""


class Square():
    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Sets the necessary attributes for the Square object
        Args:
            size (int): size of one edge of the square.
            position (tuple): the coordinates of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Gets or sets the size of the square
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter of __size
        Args:
            value (int): the size of a size of the square
        Returns:
            None
        """
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """Get or set the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is tuple \
                and len(value) is 2 and \
                type(value[0]) is int and \
                type(value[1]) is int and \
                value[0] >= 0 and \
                value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """
        Prints the squares
        Returns:
            None
        """
        if self.__size > 0:
            for y in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
        else:
            print()
