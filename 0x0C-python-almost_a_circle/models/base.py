#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This is base module.
This module provides a Base Class
"""


class Base:
    """This is a Base Class
    Attributes:
        __nb_objects: Base private attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """This is a Costructor method for Base
        Args:
            id (int): this is Base parameter
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
