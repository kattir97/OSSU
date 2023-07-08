# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 18:18:40 2023

@author: Kemokatt
"""

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')
            
    def intersect(self, other):
        longest = None
        if len(self.vals) > len(other.vals):
            longest = self.vals.copy()
        else:
            longest = other.vals.copy()
        
        new_list = []
        
        for e in longest:
            if e in self.vals and e in other.vals:
                new_list.append(e)
            
        return '{' + ','.join([str(e) for e in new_list]) + '}'
    
    def __len__(self):
        return len(self.vals)


    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    
first = intSet()
second = intSet()
first.insert(1)
first.insert(2)
first.insert(3)
second.insert(3)
second.insert(4)
second.insert(5)
    