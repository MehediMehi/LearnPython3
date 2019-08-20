#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 19:56:32 2019

@author: Mehedi Hasan Akash
"""

print(5 < 6)
print(5 > 6)
print(5 <= 6)
print(5 <= 5)
print(6 >= 5)
print(6 >= 6)
print(6 >= 7)
print(5 == 5)
print(5 == 6)
print(6 != 7)
print(6 != 6)
x, y = 5, 6 
print(id(x))
print(id(y))
print(x is y) # check object ids not values
print(x is not y)
y = 5 # immutable objects has same id for same object value
print(id(y))
print(x is y)
x, y = [5], [5] # mutable object has different ids
print(id(x))
print(id(y))
print(x == y)
print(x is y)
print(x is not y)