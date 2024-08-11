#!/usr/bin/python3
"""
   In a text file, there is a single
   character H. Your text editor can
   execute only two operations in
   this file: Copy All and Paste.

   Given a number n, write a method
   that calculates the fewest number
   of operations needed to result in
   exactly n H characters in the file.

   Prototype: def minOperations(n)
   Returns an integer
   If n is impossible to achieve, return 0
"""


def isprime(n):
    """This function check if the element is a prime number"""

    i = 2
    if n <= 1:
        return False

    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def minOperations(n):
    """ The number is either 1, a prime number or divisble by 2, 3, 5 qnd 7 """

    list_num = [2, 3, 5, 7]

    if isprime(n) or n == 1:
        return f"Min number of operations to reach {n} characters: {n}"

    elif n <= 0:
        return 0

    else:
        list_addition = []
        while list_num:
            div = list_num.pop()

            if n % div == 0:
                addition = div + (n / div)
                list_addition.append(int(addition))
        return list_addition[0]
