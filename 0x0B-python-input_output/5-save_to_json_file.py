#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This is a 5-save_to_json_file module
"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file,
    using JSON representation
    """
    with open(filename, 'w', encoding="utf-8") as wf:
        return wf.write(json.dumps(my_obj))
