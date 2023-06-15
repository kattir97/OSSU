# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 13:06:22 2023

@author: Kemokatt
"""

def payDebt(balance, annualInterestRate, monthlyPaymentRate):
    """
    Calculate the remaining balance after one year of minimum monthly payments.

    Parameters:
        balance: The initial balance on the credit card.
        annual_interest_rate: The annual interest rate as a decimal.
        monthly_payment_rate: The minimum monthly payment rate as a decimal.

    Returns:
        float: The remaining balance after one year.

    """

    monthlyInterestRate = annualInterestRate / 12.0
    
    for i in range(1, 13):
        minMonthlyPay = monthlyPaymentRate * balance
        balance = balance - minMonthlyPay
        balance = balance + (monthlyInterestRate * balance)
    
    balance = round(balance, 2)
    print('Remaining balance: ', balance)
        
        
        
payDebt(484, 0.2, 0.04)
        
    
    
    