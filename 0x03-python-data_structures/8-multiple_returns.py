#!/usr/bin/python3

def multiple_returns(sentence):
    """
    function that returns a tuple with the length
    of a string and its first character.
    """
    info_tuple = len(sentence), sentence[0]

    if len(sentence) == 0:
        info_tuple[1] = None

    return (info_tuple)
