# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 22:40:07 2023

@author: Kemokatt
"""

def payDebtV2(balance, annualInterestRate):
    """
    Calculate the lowest fixed monthly payment needed to pay off a debt within one year.

    Parameters:
        balance: The initial balance on the credit card.
        annualInterestRate: The annual interest rate as a decimal.

    Returns:
        None. Prints the lowest fixed monthly payment required to pay off the debt.

    """
    budget = balance 
    monthlyInterestRate = annualInterestRate / 12.0
    fixedPay = 0
    while budget > 0:
        budget = balance
        fixedPay += 10
        for i in range(1, 13):
            budget = budget - fixedPay
            budget = budget + (monthlyInterestRate * budget)
    print('Lowest Payment: ', fixedPay)
        
        
payDebtV2(3926, 0.2)
            