# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 09:10:54 2023

@author: Kemokatt
"""

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    
    def __eq__(self, o):
        if self.x == o.x and self.y == o.y:
            return True
        else:
            return False
    def __repr__(self):
        return "Coordinate(" + str(self.x) + "," + str(self.y) + ")"