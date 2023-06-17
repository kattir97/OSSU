# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 23:10:15 2023

@author: Kemokatt
"""

def payDebtV3(balance, annualInterestRate):
    """
    Calculate the minimum fixed monthly payment required to pay off a debt within a year.

    Parameters:
        balance (float): The initial balance on the credit card.
        annualInterestRate (float): The annual interest rate as a decimal.

    Returns:
        None. Prints the lowest monthly payment required to pay off the debt within a year.

    """
    monthlyInterestRate = annualInterestRate / 12.0
    lowerBound = balance / 12
    upperBound = balance * ((1 + monthlyInterestRate)**12) / 12.0
    budget = balance
    fixedPay = (lowerBound + upperBound) / 2
    while abs(budget) > 0.01:
        budget = balance
        for i in range(1, 13):
            budget = budget - fixedPay
            budget = budget + (monthlyInterestRate * budget)
        if budget > 0:
            lowerBound = fixedPay
        else:
            upperBound = fixedPay
        fixedPay = fixedPay = (lowerBound + upperBound) / 2
        
    fixedPay = round(fixedPay, 2)
    print('Lowest Payment: ', fixedPay)
        
        
payDebtV3(999999, 0.18)