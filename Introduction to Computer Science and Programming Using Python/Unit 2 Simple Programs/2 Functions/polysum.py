# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 15:27:45 2023

@author: Kemokatt
"""

import math

def polysum(n, s):
    '''
    n: number of sides
    s: side length
    
    returns: sum the area and square of the perimeter of the regular polygon 
    rounded to 4 decimal places
    '''
    area = (0.25 * n * s**2) / math.tan(math.pi / n)
    perimeter = (n * s) ** 2
    # sum of the area and square of the perimeter
    result = round(area + perimeter, 4)
    return result


