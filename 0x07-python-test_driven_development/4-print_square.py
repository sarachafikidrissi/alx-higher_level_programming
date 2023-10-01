#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This is the 4-print_square module.

this 4-print_square module supplies one function, print_square().
"""


def print_square(size):
    """
    A function that prints a square
    Args:
        size (int): size of square
    Raises:
        TypeError: Exception if argument is not an integer
        ValueError: Exception if argument is less than zero
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
