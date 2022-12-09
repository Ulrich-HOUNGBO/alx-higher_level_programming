#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        new = []
        for i in matrix:
            new.append(list(map(lambda x: x**2, i)))
        return (new)
    return None
