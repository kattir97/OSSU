# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 18:30:53 2023

@author: Kemokatt
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    else:
        result = base
        while exp > 1:
            result *= base 
            exp -=  1
        return result
        