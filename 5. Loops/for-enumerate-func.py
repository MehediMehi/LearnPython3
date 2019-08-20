#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 13:54:04 2019

@author: Mehedi Hasan Akash
"""

def main():
    fh = open('lines.txt')
    for index, line in enumerate(fh.readlines()): # container object like lists and strings
        print(index, line, end="") # all container type in python are iterators
    
    s = "this is a string"
    for i, c in enumerate(s): # enumerate returns 2 values, first is index and second is value
        print(i, c) # printing the whole s with index
        if c == 's': print("index {} is an s".format(i)) # print the index only for 's'

if __name__ == "__main__": main()