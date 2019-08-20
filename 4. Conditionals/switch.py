#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 13:17:39 2019

@author: Mehedi Hasan Akash
"""

def main():
    choice = dict(
            one = "first",
            two = "second",
            three = "third",
            four = "forth",
            five = "fifth"
            )
    v = 'three'
    print(choice[v])
    v = 'seven' # seven is not in the dictionary
    print(choice.get(v, 'other')) # to handle the exception we use get method
    # if get does not find the value in the dict it returns whatever after comma 
    v = 'five'
    print(choice.get(v, 'other'))

if __name__ == "__main__": main()