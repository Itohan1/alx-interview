#!/usr/bin/python3
"""
   You have n number of locked
   boxes in front of you. Each
   box is numbered sequentially
   from 0 to n - 1 and each box
   may contain keys to the other boxes
"""


def canUnlockAll(boxes):
    """Write a method that determines if all the boxes can be opened"""

    n = len(boxes)

    opened = set()
    opened.add(0)

    stack = list(boxes[0])

    while stack:
        key = stack.pop()
        if key < n and key not in opened:
            opened.add(key)
            stack.extend(boxes[key])

    return len(opened) == n
