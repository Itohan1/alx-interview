#!/usr/bin/python3
"""Given an n x n 2D matrix, rotate it 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """Rotate 2D Matrix"""

    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n - j - 1] = matrix[
                    i][n - j - 1], matrix[i][j]
