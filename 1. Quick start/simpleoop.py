#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 19:20:01 2019

@author: Mehedi Hasan Akash
"""
#simple fibonacci series

class Fibonacci():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def series(self):
        while(True):
            yield(self.b)
            self.a, self.b = self.b, self.a + self.b

f = Fibonacci(0, 1)
for r in f.series():
    if r > 100: break
    print(r, end=' ')
