# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 13:11:45 2023

@author: Kemokatt
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    middleIdx =  len(aStr) // 2
    if len(aStr) == 0:
        return False
    elif len(aStr) == 1:
        return char == aStr[middleIdx]
    elif char == aStr[middleIdx]:
        return True
    else:
        if char > aStr[middleIdx]:
            return isIn(char, aStr[middleIdx : len(aStr)])
        else:
            return isIn(char, aStr[0: middleIdx])
        
        

        
    
            