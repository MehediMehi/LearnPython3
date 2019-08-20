#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 19:10:22 2019

@author: Mehedi Hasan Akash
"""
#generator function generates an iterator which is suitable for use in a for loop
#generator is unlike other functions but has yield keyword in it and works 
#from the next line of the yield from the other calls than the first one


def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

def primes(n = 1):
    while(True):
        if isprime(n): yield n
        n += 1

for n in primes():
    if n > 100: break
    print(n)
