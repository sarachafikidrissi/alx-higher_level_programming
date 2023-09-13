#!/usr/bin/python3

def best_score(a_dictionary):
    """
    function that returns a key with the biggest integer value.
    """
    if a_dictionary is None:
        return None
    b = sorted(a_dictionary.items(), key=lambda item: item[1], reverse=True)
    a = list(dict(b))
    return (a[0])
