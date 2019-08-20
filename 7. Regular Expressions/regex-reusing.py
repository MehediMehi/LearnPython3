#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 12:50:42 2019

@author: Mehedi Hasan Akash
"""
# pre compiled regular expression
# good for using regex in a loop or more than once
# compiles before going into loops which lowers work for compiling again and again in loops

import re

def main():
     fh = open('raven.txt')
     # pre compiled (pattern)
     pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE) # ignores the case difference
     for line in fh:
         if re.search(pattern, line):
             print(pattern.sub('###', line), end='') # substitution if matches and convert into ###

if __name__ == "__main__": main()
             