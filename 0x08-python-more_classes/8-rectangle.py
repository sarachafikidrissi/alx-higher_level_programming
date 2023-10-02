#!/usr/bin/python3

# -*- coding: utf-8 -*-
"""
This is 0-rectangle.py module
in this module there is a class called rectangle().
"""


class Rectangle:
    """class Rectangle that defines a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Init method for Rectangle

        Attributes:
            width (int, optional): the width of rectangle
            height (int, optional): the height of rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """str method to print rectangle
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string

        for i in range(self.__height):
            for j in range(self.__width):
                string += str(self.print_symbol)
            if i < self.__height - 1:
                string += '\n'
        return string

    def __repr__(self):
        """
        provides __repr__ method for object rectangle

        Returns:+
            string (str): string to get
        """
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height) +\
            ")"

    def __del__(self):
        """
        delete method for rectangle
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Method to compare 2 rectangles

        Attributes:
            rect_1 (class Rectangle): Rectangle 1 must be an instance rectangle
            rect_2 (class Rectangle): Rectangle 2 must be an instance rectangle

        Raises:
            TypeError: If rect_1 or rect_2 aren't instance of rectangle

        Returns:
            The biggest rectangle
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
