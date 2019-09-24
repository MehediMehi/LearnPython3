#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 16:16:57 2019

@author: Mehedi Hasan Akash
"""

def main():
    testfunc1()
    testfunc(42)
    testfunc(42, 48)
    testfunc(42, 52, 62) # passed values will replace default values in function parameter
    testfunc2(32)
    testfunc2(32, 38)
    testfunc2(32, 42, 52)
    testfunc3()
    testfunc3(9, 8, 7)
    testfunc3(9, 8, 7, 6, 5)
    testfunc4(1, 2, 3)
    testfunc4(1, 2, 3, 4)
    testfunc4(1, 2, 3, 4, 5, 6, 7, 8)
    testfunc5(one = 1, two = 2, four = 42)
    testfunc6(5, 6, 7, 8, 9, 10, one = 1, two = 2, three = 3, four = 42)

def testfunc1():
    pass # will resolve empty function body problem

def testfunc(number, another = None, onemore = 44): # put default values to solve function calling problems with less than argument number calling (example: testfunc(42)
    print('testfunc:')
    print("This is a test function", number, another, onemore)

def testfunc2(number, another = None, onemore = 44):
    print('testfunc2:')
    if another is None: # None is checkable (singletone Object)
        another = 100
    print('This is a test function', number, another, onemore)

def testfunc3(*args): # arbitary list of arguments
    print('testfunc3:')
    print(args)

def testfunc4(this, that, other, *args): # args works as a tuple
    print()
    print('testfunc4:')
    print(this, that, other, args)
    for n in args: print(n, end=' ')
    print()

def testfunc5(**kwargs): # keyword arguments, works as a dictionary
    print('testfunc5:')
    print('values', kwargs['one'], kwargs['two'], kwargs['four'])

def testfunc6(this, that, other, *args, **kwargs): # only restriction is here you have to follow the order if you use all (like first simple arguments, then *args and finally **kwargs)
    print('testfunc6:')
    print(this, that, other, args, kwargs)
    print()
    for n in args: print(n) # tuple maintains the order it has been assigned
    for k in kwargs: print(k, kwargs[k]) # dictionary does not maintain order

if __name__ == "__main__": main()
