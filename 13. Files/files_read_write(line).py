#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 13:45:39 2019
@author: Mehedi Hasan Akash
Github: https://github.com/MehediMehi
"""

def main():
    infile = open('lines.txt', 'r')
    outfile = open('new.txt', 'w') # creates file if not exist and writes into
    for line in infile:
        print(line, file = outfile, end='') # print() will print into the outfile instead of screen (file parameter accepts file name)
    print("Done.") # feedback in the screen

if __name__ == "__main__": main()