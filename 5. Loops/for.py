#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 13:42:47 2019

@author: Mehedi Hasan Akash
"""
# for loop works with iterators

def main():
    fh = open('lines.txt')
    for line in fh.readlines(): # container object like lists and strings
        print(line, end="") # all container type in python are iterators

if __name__ == "__main__": main()