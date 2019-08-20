#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 11:02:48 2019

@author: Mehedi Hasan Akash
"""

def main():
    for n in primes(): # generate a list of prime numbers
        if n > 100: break
        print(n)

def isprime(n):
    if n == 1: # one is never prime
        return False
    for x in range(2, n):
        if n % x == 0:
            return False # found a divisor, not prime
    else:
        return True

def primes(n = 1):
    while(True):
        if isprime(n): yield n # yield makes this a generator
        n += 1

if __name__ == "__main__": main()
