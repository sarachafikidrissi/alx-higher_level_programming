#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""This 3-is_kind_of_class Module
it supplies one fucntion: is_kind_of_class()
"""


def is_kind_of_class(obj, a_class):
    """A function that checks if object is an instance of,
    or if the object is an instance of a
    class that inherited from, the specified clas
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
