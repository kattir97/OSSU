# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 10:18:56 2023

@author: Kemokatt
"""

def gcdRecur(a, b): #9, 12
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)
        
            
        