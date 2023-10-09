#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This is 5-base_geometry Class
"""


class BaseGeometry:
    """
    Raises:
        Exception: area() is not implemented
        TypeError: in case value is not integer
        ValueError: in case value is less or equal than zero
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        elif value <= 0:
            raise ValueError(name + " must be greater than 0")
