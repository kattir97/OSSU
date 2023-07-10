# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 14:27:52 2023

@author: Kemokatt
"""



def genPrimes():
    primes = []
    num = 2 
    isPrime = None
    while True:
        if num == 2:
            yield num
            num += 1
        for i in range(2, num):
            if num % i != 0:
                isPrime = True
            else:
                isPrime = False
                break
                
        if isPrime:
            primes.append(num)
            yield num
        
        num += 1
            

prime = genPrimes()
                