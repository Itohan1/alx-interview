#!/usr/bin/python3
"""
    Given a pile of coins of different values,
    determine the fewest number of coins
    needed to meet a given amount total
"""


def makeChange(coins, total):
    """
        coins is a list of the values of the
        coins in your possession
    """

    q = 0
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    remain = total
    for i in coins:
        if i <= remain:
            num = remain // i
            q += num
            remain -= num * i

        if remain == 0:
            break

    if remain > 0:
        return -1

    return q
