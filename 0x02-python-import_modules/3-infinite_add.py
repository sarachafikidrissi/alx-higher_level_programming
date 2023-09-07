#!/usr/bin/python3

import sys

if __name__ != "__main__":
    exit()

num_args = len(sys.argv) - 1
total = 0

if num_args == 0:
    print(num_args)

else:
    for n in range(1, num_args + 1):
        total += int(sys.argv[n])
    print(total)
