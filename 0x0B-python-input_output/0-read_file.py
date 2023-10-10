#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This is a 0-read_file module
"""


def read_file(filename=""):
    """read a text file (UTF8) and prints it to stdout
    """
    with open(filename, 'r', encoding="utf-8") as f:
        f_read = f.read()
        print(f_read, end='')
