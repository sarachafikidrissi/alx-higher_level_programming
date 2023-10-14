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
        self.y = y

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
    def width(self, width_value):
        """Setter width of the rectangle
        Attributes:
            width_value (int): the width value of rectangle
        """
        if type(width_value) is not int:
            raise TypeError("width must be an integer")
        elif width_value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width_value

    @height.setter
    def height(self, height_value):
        """Setter height of the rectangle
        Attributes:
            height_value (int): the height value of rectangle
        """
        if type(height_value) is not int:
            raise TypeError("height must be an integer")
        elif height_value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height_value

    @x.setter
    def x(self, value):
        """Setter x of the rectangle
        Attributes:
            value (int): the x value of rectangle
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")

        else:
            self.__x = value

    @y.setter
    def y(self, value):
        """Setter y of the rectangle
        Attributes:
            value (int): the y value of rectangle
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Calculates the area of a rectangle
        Returns:
            The area of Rectangle
        """
        return self.__height * self.__width

    def display(self):
        """Prints the character '#'.
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            for _ in range(self.__x):
                print(' ', end='')
            for _ in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """This is special method __str__()
        Returns:
            [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return ('[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.__x,
                self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """updates rectangle class.
        Attributes:
            args (list): inputted arguments to updating rectangle class
            kwargs (dict): inputted arguments tu updating rectangle class
        """
        if args:
            self.id = args[0] if len(args) > 0 else self.id
            self.__width = args[1] if len(args) > 1 else self.__width
            self.__height = args[2] if len(args) > 2 else self.__height
            self.__x = args[3] if len(args) > 3 else self.__x
            self.__y = args[4] if len(args) > 4 else self.__y
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            self.__width = kwargs.get('width', self.__width)
            self.__height = kwargs.get('height', self.__height)
            self.__x = kwargs.get('x', self.__x)
            self.__y = kwargs.get('y', self.__y)
