#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""This is a 2-append_write module
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8) and
    returns the number of characters added.
    """
    with open(filename, 'a', encoding="utf-8") as wf:
        wf.write(text)
        readed_char = wf.tell()
    return (readed_char)
