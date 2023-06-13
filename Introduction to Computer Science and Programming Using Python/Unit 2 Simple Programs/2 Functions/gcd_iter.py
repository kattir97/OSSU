# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 21:15:33 2023

@author: Kemokatt
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    divisor = None
    num = max(a, b)
    for i in range(1, num + 1):
        if a % i == 0 and b % i == 0:
            divisor = i
    return divisor

