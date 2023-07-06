# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 14:11:56 2023

@author: Kemokatt
"""

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function
    remained = hand.copy()
    
    for letter in word:
        if letter in remained and remained[letter] > 1:
            remained[letter] -= 1
        else:
            del(remained[letter])
            
        
    return remained