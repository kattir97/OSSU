# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 16:05:32 2023

@author: Kemokatt
"""

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    
    total = 0
    for i in hand:
        total += hand[i]
    return total