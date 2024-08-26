#!/usr/bin/python3
"""
    Write a method that determines
    if a given data set represents
    a valid UTF-8 encoding.
"""


def validUTF8(data):
    """True if data is a valid UTF-8 encoding, else return False"""

    n = 0
    for v in data:
        if n > 0:
            if v >> 6 == 10:
                return True
            else:
                return False
            n -= 1
        elif n == 0:
            if v >> 7 == 0:
                continue
            if v >> 5 == 110:
                n = 1
            if v >> 4 == 1110:
                n == 2
            if v >> 3 == 11110:
                n = 3
        else:
            return False
        n += 1

    if n != 0:
        return False
    else:
        return True
