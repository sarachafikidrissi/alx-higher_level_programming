#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
    function that prints a dictionary by ordered keys.
    """

    [print("{}: {}".format(i, a_dictionary[i])) for i in sorted(a_dictionary)]
