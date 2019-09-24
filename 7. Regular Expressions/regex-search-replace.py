#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 12:38:46 2019

@author: Mehedi Hasan Akash
"""

import re

def main():
    fh = open('raven.txt')
    # search and replace (re.sub)
    for line in fh:
        print(re.sub('(Len|Neverm)ore', '####', line), end='')
        
        # string replace method
        match = re.search('(Len|Neverm)ore', line)
        if match:
            print(line.replace(match.group(), '###'), end='')

if __name__ == "__main__": main()
