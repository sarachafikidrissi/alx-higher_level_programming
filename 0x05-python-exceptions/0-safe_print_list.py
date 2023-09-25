#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    total_printed = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            total_printed += 1
        except IndexError:
            continue
    print()
    return (total_printed)
