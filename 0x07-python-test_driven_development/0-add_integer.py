#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This is the 0-add_integer pyhton file.

The 0-add_integer supplies one function, add_integer(a, b=98).
"""

def add_integer(a, b=98):

    """This function adds 2 integers.
    Args:
        a (int): First integer
        b (int): Second integer
    Raises:
        TypeError: Exception if size is not an integer
    """

    if type(a) is not int:
        if type(a) is float and a == a and abs(a) <= 1.7976931348623158e+308:
            a = int(a)
        else:
            raise TypeError("a must be an integer")
    if type(b) is not int:
        if type(b) is float and b == b and abs(b) <= 1.7976931348623158e+308:
            b = int(b)
        else:
            raise TypeError("b must be an integer")
    return (a + b)
