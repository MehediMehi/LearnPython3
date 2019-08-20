#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 11:35:17 2019

@author: Mehedi Hasan Akash
"""

def main():
    # conditional executions
    
    a, b = 1, 1
    if a < b:
        print("a is less than b")
    elif a > b:
        print("a is grater than b")
    else:
        print("a is equal to b")
    
    # conditional expression / conditional value
    
    a, b = 0, 1
    s = "less than" if a < b else "not less than"
    print(s)
    
if __name__ == "__main__": main()