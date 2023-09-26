#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
created on Tue September 26 2023
@author: Sara Chafik Idrissi
"""


class Square:
    """Class Square that defines a square

    Attributes :
        size (int): The size of square
    """
    def __init__(self, size=0):
        """
        The __init__ method for the square

        Args:
            size: (:obj: 'int'): A private instance size

        Raises:
            TypeError: Exception if size is not an integer
            ValueError: Exception if size is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        calculates the area of the square

        Returns:
            The square area
        """
        return self.__size ** 2
