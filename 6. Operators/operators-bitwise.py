#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 19:30:49 2019

@author: Mehedi Hasan Akash
"""

print(5)
print(0b0101)
def b(n): print('{:08b}'.format(n)) # func to print bin values upto 8 bits (:08b)
b(5)
x, y = 0x55, 0xaa # assigning binary values but inserts equivalent decimal
print(x, y) # prints equivalent decimal values
b(x) # bin value of x
b(y) # bin value of y
b(x | y) # or operation
b(x & y) # and operation
b(x ^ y) # xor operation
b(x ^ 0)
b(x ^ 1)
b(x << 4) # left shift
b(x >> 4) # right shift
b(~ x) # 1st compliment (unary operator)