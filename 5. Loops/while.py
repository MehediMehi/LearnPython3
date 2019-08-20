#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 13:34:24 2019

@author: Mehedi Hasan Akash
"""
# simple fibonacci series

def main():
    a, b = 0, 1
    while b < 50:
        print( b, end=" ")
        a, b = b, a + b

if __name__ == "__main__": main()