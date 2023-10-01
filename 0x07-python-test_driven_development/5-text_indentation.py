#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This is the 5-text_indentation module.
this modele supplies one function, text_indentation().
"""


def text_indentation(text):
    """This fucntion prints text with 2 new lines after
    each of these characters: ., ? and :

    Args:
        text (str): the text to be printed

    Raises:
        TypeError: Exception for argument that is not string
    """
    if type(text) is str:
        for i in range(len(text)):
            if text[i] in {'.', '?', ':'}:
                print(text[i])
                print()
            else:
                if text[i] == " " and text[i - 1] in {'.', '?', ':', " "}:
                    continue
                print(text[i], end="")
    else:
        raise TypeError("text must be a string")
