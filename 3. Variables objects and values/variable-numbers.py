#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 19:43:51 2019

@author: Mehedi Hasan Akash
"""

def main():
    num = 42 # integer number
    print(type(num), num)
    num = 42.0 # float number
    print(type(num), num)
    num = 42 / 9 # divide and get float value
    print(type(num), num)
    num = 42 // 9 # divide but get integer value
    print(type(num), num)
    num = round(42 / 9) # divide and get rounded integer value
    print(type(num), num)
    num = 42 % 9 # find remainder
    print(type(num), num)
    num = int(42.9) # convert into integer
    print(type(num), num)
    num = float(42) # convert into float 
    print(type(num), num)
    

if __name__ == "__main__": main()