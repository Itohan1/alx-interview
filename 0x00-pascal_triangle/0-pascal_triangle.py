#!/usr/bin/python3
"""
returns a list of lists of integers
representing the Pascal’s
triangle of n
"""


def pascal_triangle(n):
    """representing the Pascal’s"""

    last = 1
    if n <= 0:
        return []

    big = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(big[i-1][j - 1] + big[i-1][j])
        row.append(last)
        big.append(row)
    return big
