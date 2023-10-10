#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This is a 6-load_from_json_file module
"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”
    """
    with open(filename, encoding="utf-8") as rf:
        return (json.loads(rf.read()))
