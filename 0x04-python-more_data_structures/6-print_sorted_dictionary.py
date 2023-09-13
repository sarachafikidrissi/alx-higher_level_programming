#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
    function that prints a dictionary by ordered keys.
    """
    
    sorted_a = {}

    for i in sorted(a_dictionary):
        sorted_a[i] = a_dictionary[i]

    for i, j in sorted_a.items():
        print(i, ":", j)
