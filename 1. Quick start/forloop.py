#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 18:53:13 2019

@author: Mehedi Hasan Akash
"""
#reaf the fles from the file

fh = open('lines.txt', 'r')
for line in fh.readlines():
    print(line, end = '')
