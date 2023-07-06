# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 01:23:14 2023

@author: Kemokatt
"""

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    user_input = None
    last_hand = None
    while user_input != 'e':   
        user_input = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if user_input == 'n':
            new_hand = dealHand(HAND_SIZE)
            last_hand = new_hand
            playHand(new_hand, wordList, HAND_SIZE)
            print()
        elif user_input == "r":
            if last_hand == None:
                print('You have not played a hand yet. Please play a new hand first!')
                print()
                continue
            else:
                playHand(last_hand, wordList, HAND_SIZE)
        elif user_input == "e":
            break
        else:
            print('Invalid command.')