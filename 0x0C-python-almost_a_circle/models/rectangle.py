#!/usr/bin/python3
"""Module that contains class Rectangle,
inheritance of class Base.
"""

class Rectangle(Base):
    """Class Rectangle."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize instances."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)


    @property
    def width(self):
        """Gets the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width value

    @property
    def height(self):
        """Gets the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets x."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets y."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle object."""
        return self.width * self.height

    def display(self):
        """Displays a rectangle."""
        rectangle = self.y * "\n"
        for i in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"
        print(rectangle, end='')

    def __str__(self):
        """str special method."""
        str_rectangle = "[Rectangle] "
        str_id = "({}) ".format(self.id)
        str_wh = "{}/{}".format(self.width, self.height)
        str_xy = "{}/{} - ".format(self.x, self.y)
        return str_rectangle + str_id + str_wh + str_xy

    def update(self, *args, **kwargs):
        """Update method."""
        if args is not None and  len(args) is not 0:
            list_atr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Method that returns a dictionary with properties."""
        list_atr = ['id', 'width', 'height', 'x', 'y']
        dict_res = {}

        for key in list_atr:
            dict_res[key] = getattr(self, key)

        return dict_res
