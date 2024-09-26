#!/usr/bin/python3
"""
    Create a function returns the
    perimeter of the island described in grid
"""


def closed_perimeter(grid):
    """Check closed parameter"""
    new_list = []
    main_list = []
    k = 0
    for i in grid:
        if k != 0 and k != len(grid) - 1:
            for j in range(len(i)):
                if j == 0 and i[j] == '0':
                    continue
                elif j > 0 and j < len(i) - 1:
                    new_list.append(i[j])
                elif (j == 0 and i[j] == '1') or \
                        (j == len(i) - 1 and i[j] == '1'):
                    return('Not a grid')
            main_list.append(new_list)
            new_list = []
        k += 1
    return main_list


def island_perimeter(grid):
    """Island Perimeter"""

    new_grid = closed_perimeter(grid)

    k = 0
    for i in new_grid:
        k += 1
    return k * len(i)
