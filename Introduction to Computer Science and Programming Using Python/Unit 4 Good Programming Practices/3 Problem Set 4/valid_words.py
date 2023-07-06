# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 16:01:19 2023

@author: Kemokatt
"""

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """    
    new_hand = hand.copy();
    
    def isComposed():
        for letter in word:
            if letter not in new_hand or new_hand[letter] == 0:
                return False
            else:
                new_hand[letter] -= 1
        return True
    
    if word in wordList and isComposed() == True:
        return True
    else:
        return False