#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""This is a 3-to_json_string module
"""
import json


def to_json_string(my_obj):
    """encoding a python object to JSON
    Arguments:
        my_obj (str): The inputed object to convert into json
    Return:
        A json format text
    """
    json_data = json.dumps(my_obj)
    return json_data
