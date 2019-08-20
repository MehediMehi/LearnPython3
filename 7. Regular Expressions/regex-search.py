#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 12:07:36 2019

@author: Mehedi Hasan Akash
"""

import re

def main():
    fh = open('raven.txt')
    # search (re.search)
    for line in fh:
        
        # print the whole line
        if re.search('(Len|Neverm)ore', line):
            print(line, end='')
        
        # print only matched parts
        match = re.search('(Len|Neverm)ore', line)
        if match:
            print(match.group())
    
        
    
if __name__ == "__main__": main()