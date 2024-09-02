#!/usr/bin/python3
"""Solve the Nqueens problem"""
import sys
import random


def print_solution(bod):
    """Print a solution"""
    print([[i, row.index(1)] for i, row in enumerate(bod)])


def check_safety(bod, row, col, N):
    """Check for validity"""

    for i in range(col):
        if bod[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if bod[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if bod[i][j] == 1:
            return False

    return True


def sol_queen(bod, col, N):
    """Use backtracking to identity all solutions in nqueen"""

    if col >= N:
        print_solution(bod)
        return True

    res = False

    for i in range(N):
        if check_safety(bod, i, col, N):
            bod[i][col] = 1
            res = sol_queen(bod, col + 1, N) or res
            bod[i][col] = 0
    return res


def Nqueen():
    """Solve Nqueen problems"""

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    bod = [[0] * N for _ in range(N)]
    sol_queen(bod, 0, N)


if __name__ == "__main__":
    Nqueen()
