#!/usr/bin/python3
import sys

num_args = len(sys.argv) - 1

if __name__ == "__main__":
    
    if num_args == 0:
        print("0 arguments")

    else:
        if num_args == 1:
            str = "argument"
        else:
            str = "arguements"

        print("{:d} {:s}:".format(num_args, str))
        for n in range(1, (num_args + 1)):
            print("{:d}:".format(n), sys.argv[n])
