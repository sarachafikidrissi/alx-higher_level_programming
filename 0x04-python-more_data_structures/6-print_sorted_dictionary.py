#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
    function that prints a dictionary by ordered keys.
    """

    sorted_a = dict(sorted(a_dictionary.items()))

    for i, j in sorted_a.items():
        print(i, ":", j)
