#!/usr/bin/python3

# -*- coding: utf-8 -*-
"""
This is 0-rectangle.py module
in this module there is a class called rectangle().
"""


class Rectangle:
    """class Rectangle that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Init method for Rectangle

        Attributes:
            width (int, optional): the width of rectangle
            height (int, optional): the height of rectangle"""
        self.width = width
        self.height = height

    def __str__(self):
        """str method to print rectangle
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string

        for i in range(self.__height):
            for j in range(self.__width):
                string += '#'
            if i < self.__height - 1:
                string += '\n'
        return string

    @property
    def height(self):
        """Property height to retrieve it.
        Returns:
            height (int): the height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter heigth of the rectangle.
    Attributes:
        value (int): the value of rectangle height
    Raises:
        TypeError: Exception for not integer values
        ValueError: Exception for negative values
    """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """Property width to retrieve it.
        Returns:
            width (int): the width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter width of rectangle.
        Attributes:
            value (int): the width value of rectangle
        Raise:
            TypeError: Exception for not integer values
            ValueError: Exception for negative values
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """Calculate the area of rectangle
        Returns:
            The Area of Rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of rectangle
        Returns:
            The Perimeter of Rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
