# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 18:35:26 2023

@author: Kemokatt
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    
    # Your Code Here
    count = 0
    biggest = None
    for i, x in aDict.items():
        if len(x) >= count:
            count = len(x)
            biggest = i
        
    return biggest