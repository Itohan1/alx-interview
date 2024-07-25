#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for u in triangle:
        print("[{}]".format(",".join([str(x) for x in u])))

if __name__ == "__main__":
    pascal_triangle(5)
    print_triangle(pascal_triangle(5))
