#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 12:36:48 2019

@author: Mehedi Hasan Akash
"""
# immutable objects have same id for a value because they don't change 
# mutable objects has different id's as their values are changable

x = 42 # immutable
print(x)
print(id(x))
print(type(x))
print(id(42))
print(type(42))
y = 42 # immutable
print(id(y))
print(x == y) # == to test is the values are equal
print(x is y) # is to test if both are same (quality)
x = dict(x = 42) # mutable
print(type(x))
print(x)
print(id(x))
y = dict(x = 42) # mutable
print(id(y))
print(x)
print(y)
print(x == y)
print(x is y) # not same because they are different and changable

# logical values
a, b = 0, 1
print(a == b)
print(a < b)
print(a > b)
a = True
print(a)
print(type(a))
print(id(a))
b = True
print(id(b))
print(id(True))
