#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This is rectangle module.
This module provides a Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """This is Rectangle Class
    it inherits from a Base class to manage identification
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """This is constructor methode for Rectangle
        Attributes:
            width (int): Represents the width of a rectangle
            height (int): Represents the height of a rectangle
            x (int, optional): The x-coordinate of the top-left corner.
            y (int, optional): The y-coordinate of the top-left corner.
            id (int): The unique identifier for the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x

    @property
    def width(self):
        """Property width to retrieve it.
        Returns:
            width (int): The width of rectangle
        """
        return self.__width

    @property
    def height(self):
        """Property height to retrieve it.
        Returns:
            height (int): The height of rectangle
        """
        return self.__height

    @property
    def x(self):
        """Property x to retrieve it.
        Returns:
            x (int): the x-coordinate
        """
        return self.__x

    @property
    def y(self):
        """Property y to retrieve it.
        Returns:
            y (int): the y-coordinate
        """
        return self.__y

    @width.setter
    def width(self, value):
        """Setter width of the rectangle
        Attributes:
            value (int): the width value of rectangle
        """
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter height of the rectangle
        Attributes:
            value (int): the height value of rectangle
        """
        self.__height = value

    @x.setter
    def x(self, value):
        """Setter x of the rectangle
        Attributes:
            value (int): the x value of rectangle
        """
        self.__x = value

    @y.setter
    def y(self, value):
        """Setter y of the rectangle
        Attributes:
            value (int): the y value of rectangle
        """
        self.__y = value
