#!/usr/bin/python3
"""Defining a class rectangle"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """ Inititalizing a new rectangle

        Args:
            width: is width of the rectangle
            height: is the height of the rectangle
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """Get width of rectangle"""

            return self.__width

        @property.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError(width must be an integer)
            if (value < 0):
                raise ValueError(width must be >= 0)
            self.__width = value

        @property
        def height(self):
            """Get height of rectangle"""

            return self.__height

        @property.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError(height must be an integer)
            if (value < 0):
                raise ValueError(height must be >= 0)
            self.__height = value
