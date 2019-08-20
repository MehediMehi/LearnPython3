#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 10:50:20 2019

@author: Mehedi Hasan Akash
"""
# assignment operator assigns an object in python and if that
# is not already created it creates before assigning value

def main():
    a = 1 # assignment operator creates object as the same type of the value given
    b = "one"
    print(a)
    print(type(b), b)
    c, d = 0, 1
    c, d = d, c # swap values without temporary variable
    print(c, d)
    e = (1, 2, 3, 4, 5) # this is tuple in python
    print(type(e), e) # prints as accetable form for tuple
    f = [1, 2, 3, 4, 5] # this is list in python (works like array)
    print(type(f), f) # prints as accetable form for list
    print("This is the syntax.py file.")
    egg()

def egg():
    print("egg.")

if __name__ == "__main__": main()
