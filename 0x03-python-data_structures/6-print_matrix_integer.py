#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    """
    function that prints a matrix of integers
    """
    for row in matrix:
        row_len = len(row)
        for j in range(row_len):
            if j != row_len - 1:
                print("{:d}".format(row[j]), end=' ')
            else:
                print("{:d}".format(row[j]), end='')
        print()
