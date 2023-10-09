#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This is a my_list Model it
supplies one function printed_sorted()
"""


class MyList(list):
    """
    This is a class MyList that inherits from another class named list
    """
    def print_sorted(self):
        """
        Pyblic instance method that prints sotred list
        """
        new_list = self[:]
        new_list.sort()
        print(new_list)
