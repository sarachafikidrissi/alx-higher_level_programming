#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on 3-10-2023
@author: sara chafik idrissi"""


class LockedClass:
    """A locked class that only lets the user dynamically create the instance
    attribute 'first_name'"""
    __slots__ = ['first_name']
