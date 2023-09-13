#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    function that adds all unique integers in a
    list (only once for each integer).
    """
    if my_list is None:
        return None
    add = 0
    new_list = list(set(my_list))

    for i in range(len(new_list)):
        add += new_list[i]
        i +=1

    return (add)
