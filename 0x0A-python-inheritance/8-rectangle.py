#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This is 8-rectangle Module
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This is a Rectangle class, inherites from BaseGeometry
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
