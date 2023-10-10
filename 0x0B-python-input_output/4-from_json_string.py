#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This is a 4-from_json_string module
"""
import json


def from_json_string(my_str):
    """decoding JSON to python object
    Arguments:
        my_str (str): the inputed JSON string

    Return:
        A python object format

    """

    json_data = json.loads(my_str)
    return json_data
