#!/usr/bin/python3


def fizzbuzz():
    for j in range(1, 101):
        if j % 3 == 0:
            print("Fizz", end="")
        if j % 5 == 0:
            print("Buzz", end="")
        if j % 3 != 0 and j % 5 != 0:
            print("{:d}".format(i), end="")
        print(" ", end="")
