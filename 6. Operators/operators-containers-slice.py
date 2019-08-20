#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 11:38:35 2019

@author: Mehedi Hasan Akash
"""
# slice- [start, stop, steps] - 
# stop is non inclusive like if value 42 it will work till 42-1

list = [1,2,3,4,5,6,7,8,9,10]
print(list)
print(list[0])
print(list[9])
print(list[0:5])
print(list[4])
for i in range(0,10): print(i)
print(list[0:10])
list[:] = range(100)
print(list)
print(list[27])
print(list[27:42])
print(list[27:42:3])
for i in list[27:43:3]: print(i)
list[27:43:3] = (99,99,99,99,99,99)
print(list)
