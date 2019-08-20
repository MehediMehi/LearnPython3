#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 13:29:09 2019

@author: Mehedi Hasan Akash
"""

def main():
    a, b = 0, 1
    # regular condition
    if a < b:
        v = "this is true"
    else:
        v = 'this is not true'
    print(v)
    
    # conditional expression
    v = "this is true" if a < b else "this is not true"
    print(v)

if __name__ == "__main__": main()