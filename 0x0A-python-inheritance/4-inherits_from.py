#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""This is a 4-inherits_from.py module.
it supplies one function: inherits_from()
"""


def inherits_from(obj, a_class):
    """A function that checks if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class
    """
    if not isinstance(a_class, type):
        raise TypeError("a_class must be a type")
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
