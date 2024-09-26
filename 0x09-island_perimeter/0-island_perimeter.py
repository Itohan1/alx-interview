#!/usr/bin/python3
"""
    Create a function returns the
    perimeter of the island described in grid
"""


def island_perimeter(grid):
    """Island Perimeter"""

    peri = 0

    rows = len(grid)
    column = len(grid[0])

    for r in range(rows):
        for c in range(column):
            if grid[r][c] == 1:
                if r == 0 or grid[r - 1][c] == 0:
                    peri += 1
                if r == rows - 1 or grid[r + 1][c] == 0:
                    peri += 1
                if c == 0 or grid[r][c - 1] == 0:
                    peri += 1
                if c == column - 1 or grid[r][c + 1] == 0:
                    peri += 1
    return peri
