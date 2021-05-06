#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda a: list(map(lambda x: x*x, a)), matrix))
