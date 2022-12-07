#!/usr/bin/python3
"""
Computes the square value of all integers of a matrix using map.
Returns a new matrix which same size as matrix
Each value should be the square of the value of the input
Test file is 101-main.py
"""


def square_matrix_map(matrix=[]):
    return (list(map(lambda x: list(map(lambda y: y**2, x)), matrix)))
