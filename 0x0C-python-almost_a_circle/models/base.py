#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This is base module.
This module priovides a Base Class
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns a json string representation

        Attributes:
            list_dictionaries (json): An inputted jason list of dictionaries
        Return:
            A json repreentation
        """
        if list_dictionaries is None or not list_dictionaries:
            return '[]'
        return json.dumps(list_dictionaries)
