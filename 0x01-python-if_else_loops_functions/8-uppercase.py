#!/usr/bin/python3
def uppercase(str):
    for w in str:
        char = ord(w)
        if char >= 97 and char <= 122:
            char -= 32
        print("{:c}".format(char), end="")
    print()
