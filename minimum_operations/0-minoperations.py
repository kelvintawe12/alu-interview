#!/usr/bin/python3

def minOperations(n):
    '''Check if n is less than 2, in which case it's impossible to perform the operations'''
    if n < 2:
        return 0

    operations = 0
    factor = 2

    # Prime factorization approach
    while factor * factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    # If n is still greater than 1, it must be prime
    if n > 1:
        operations += n

    return operations
