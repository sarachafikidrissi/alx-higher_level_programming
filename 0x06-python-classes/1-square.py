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
    def __init__(self, size):
        """
        The __init__ method for the square

        Args:
            size: (:obj: 'int'): A private instance size
        """
        self.__size = size
