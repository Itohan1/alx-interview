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
            if v >> 6 != 0b10:
                return False
            n -= 1
        elif n == 0:
            if v >> 7 == 0:
                continue
            if v >> 5 == 0b110:
                n = 1
            if v >> 4 == 0b1110:
                n = 2
            if v >> 3 == 0b11110:
                n = 3
        else:
            return False
    if n != 0:
        return False
    else:
        return True
