# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 22:48:47 2023

@author: Kemokatt
"""

low = 0
high = 100
res = int((low + high) / 2)
guess = None

print("Please think of a number between 0 and 100!")


while guess != "c":
    print("Is your secret number ", res, "?")
    guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if guess == "l":
        low = res
        res = int((low + high) / 2)
    elif guess == "h":
        high = res
        res = int((low + high) / 2)
    elif guess == "c":
        print("Game over. Your secret number was: ", res)
    else:
        print("Sorry, I did not understand your input.")