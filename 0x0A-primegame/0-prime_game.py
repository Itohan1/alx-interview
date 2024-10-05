#!/usr/bin/python3
"""Game theory"""


def isWinner(x, nums):
    """Finding the game winner"""

    def sieve_of_eratosthenes(n):
        """Finding the prime numbers"""

        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        return [i for i, prime in enumerate(sieve) if prime]

    maria = 0
    ben = 0

    for n in nums:
        if n == 1:
            ben += 1
            continue
        primes = sieve_of_eratosthenes(n)
        turn = 0
        remain = set(range(1, n + 1))
        for prime in primes:
            if prime in remain:
                multiples = set(range(prime, n + 1, prime))
                remain -= multiples

                turn ^= 1

        if turn == 1:
            ben += 1
        else:
            maria += 1

    if maria > ben:
        return 'Maria'

    elif ben > maria:
        return 'Ben'

    else:
        return 'Ben'
