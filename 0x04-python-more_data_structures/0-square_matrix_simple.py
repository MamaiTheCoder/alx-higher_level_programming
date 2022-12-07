#!/usr/bin/python3
"""
Computes the square value of all integers of a matrix.
Test file is 0-main.py
"""


def square_matrix_simple(matrix=[]):
    new_mat = matrix[:]

    for i in range(len(matrix)):
        new_mat[i] = list(map(lambda x: x**2, matrix[i]))
    return (new_mat)
