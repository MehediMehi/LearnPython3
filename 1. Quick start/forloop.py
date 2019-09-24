#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 18:53:13 2019

@author: Mehedi Hasan Akash
"""
#read the fles from the file

fh = open('lines.txt')
for line in fh.readlines():
    print(line, end = '')
