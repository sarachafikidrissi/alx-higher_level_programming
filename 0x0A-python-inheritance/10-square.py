#!/usr/bin/python3|
# -*- coding: utf-8 -*-

"""
this is 10-square method
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This is a Square class, inherits from Rectangle
    """
    def __init__(self, size):
        """init function for Square
        Attributes:
            size (int): size of square
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
