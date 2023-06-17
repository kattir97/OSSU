# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 13:15:53 2023

@author: Kemokatt
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    aTup = aTup[::2]
    return aTup