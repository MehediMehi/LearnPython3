#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 11:08:05 2019

@author: Mehedi Hasan Akash
"""

a, b = 0, 1
if a < b:
    print('a ({}) is less than b ({})'.format(a, b))
else:
    print('a ({}) is not less than b ({})'.format(a, b))

print("foo" if a < b else "bar")