#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""This is a 1-write_file module
"""


def write_file(filename="", text=""):
    """write a text file (UTF8) and return the number character readed
    """
    with open(filename, 'w', encoding="utf-8") as wf:
        wf.write(text)
        readed_char = wf.tell()
    return (readed_char)
