#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    function that computes the square value of all integers of a matrix.
    """
    if matrix is None:
        return None
    new_matrix = []
    def square(x):
        return (x ** 2)

    for row in matrix:
        new_row = []
        for i in row:
            new_row.append(square(i))
        new_matrix.append(new_row)
    return (new_matrix)
