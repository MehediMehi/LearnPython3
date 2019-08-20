#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 20:26:20 2019

@author: Mehedi Hasan Akash
"""

try:
    fh = open('xlines.txt')
    for line in fh.readlines():
        print(line)
except IOError as e:
    print("Something bad happened ({})".format(e))

print("After badness")