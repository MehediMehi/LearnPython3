#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 11:46:08 2019

@author: Mehedi Hasan Akash
"""

def main():
    x = (1, 2, 3) # tuple is immutable, no insertion, no update, no delete
    print(type(x), x)
    for i in x:
        print(i)
    x = [1, 2, 3] # list is mutable, insertion, update, delete is possible
    x.append(5) # add 5 at the end
    print(type(x), x)
    x.insert(0,7) # insert(in which index to insert, value to insert)
    print(type(x), x)
    for i in x:
        print(i)
    x = "string"
    print(type(x), x[2])
    print(type(x), x[2:4]) # slice gives substring, [index to begin:index before that slice stops]
    for i in x:
        print(i)

if __name__ == "__main__": main()