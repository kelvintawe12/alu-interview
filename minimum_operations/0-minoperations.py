#!/usr/bin/python3

def minOperations(n):
    """
    Module: minimum_operations
    This module provides a function to calculate the minimum number of operations 
    needed to achieve a given number n starting from 1, using a specific set of operations.
    Functions:
        minOperations(n): Returns the minimum number of operations needed to achieve n.
    """
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
