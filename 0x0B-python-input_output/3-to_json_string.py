#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""This is a 3-to_json_string module
"""


def to_json_string(my_obj):
    import json
    """encoding a python object to JSON
    """
    json_data = json.dumps(my_obj)
    return json_data
