#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This is Square module.
This module provides a Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This is Square class
    it inherits from Rectangle class to manage identification
    """
    def __init__(self, size, x=0, y=0, id=None):
        """This is constructor methode for Square
        Attributes:
            size (int): The size of Square
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """This is special method __str__()
        Returns:
            [Square] (<id>) <x>/<y> - <size>
        """
        return ('[Square] ({}) {}/{} - {}'.format(self.id,
                self.x, self.y, self.size))

    @property
    def size(self):
        """Property size to retrieve it.
        Returns:
            size (int): The width of rectangle
        """
        return self.width

    @size.setter
    def size(self, value):
        """Setter width of the rectangle
        Attributes:
            value (int): the width value of rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value

    def update(self, *args, **kwargs):
        """
        Updates Square class

        Attribute:
            args (list): inputted arguments to updating rectangle class
            kwargs (dict): inputted arguments tu updating rectangle class
        """
        if args is not None and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg

        elif kwargs is not None and len(kwargs) != 0:
            for (key, value) in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Creates a dictionary representation for Square attributes

        Return:
            A dictionary representation
        """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
