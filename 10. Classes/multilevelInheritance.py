#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 12:48:44 2019

@author: Mehedi Hasan Akash
"""
# in the case of multi-level inheritances, a Python super() will always refer the immediate superclass.

class A:
    def __init__(self):
        print('Initializing: class A')
    
    def sub_method(self, b):
        print('Printing from class A:', b)

class B(A): # B is inheriting A class
    def __init__(self):
        print('Initializing: class B')
        super().__init__()
    
    def sub_method(self, b):
        print('Printing from class B:', b)
        super().sub_method(b + 1)

class C(B): # C is inheriting B class which itself inherites A class
    def __init__(self):
        print('Initializing: class C')
        super().__init__()
    
    def sub_method(self, b):
        print('Printing from class C:', b)
        super().sub_method(b + 1)

if __name__ == '__main__':
    c = C()
    c.sub_method(1)
