#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    """
    function that prints a matrix of integers
    """
    for i in matrix:
        i_len = len(i)
        for j in range(i_len):
            if i != i_len - 1:
                print("{:d}".format(i[j]), end=" ")
            else:
                print("{:d}".format(i[j]), end=" ")
        print()
