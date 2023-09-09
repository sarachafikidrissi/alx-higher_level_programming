#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    a function that adds 2 tuples.
    """

    if len(tuple_a) < 2:
        tuple_a = tuple_a + (0,) * (2 - len(tuple_a))
    
    elif len(tuple_b) < 2:
        tuple_b = tuple_b + (0,) * (2 - len(tuple_b))

    tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return (tuple)
