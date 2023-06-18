# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 18:30:22 2023

@author: Kemokatt
"""

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    count = 0
    for value in aDict.values():
        count += len(value)
    return count
        