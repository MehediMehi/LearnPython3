#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 11:51:10 2019

@author: Mehedi Hasan Akash
"""

def main():
    func(1)
    func() #  when no argument is passed, default value will work
    func(5)

def func(a = 7): # giving argument a default value
    for i in range(a, 10):
        print(i, end=' ')
    print()        

if __name__ == "__main__": main()