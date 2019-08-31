#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:51:10 2019

@author: Mehedi Hasan Akash
"""
# generator function returns an iterator object

def main():
    print('Noninclusive range object:')
    for i in range(25): # range object is noninclusive, prints 0 to 24 but not 25
        print(i, end=' ')
    print()
    print('inclusive three arguments must func')
    for i in inclusive_range(0, 25, 1): # can not use (25) though start is defined as default
        print(i, end=' ')
    print()
    # triggers TypeError for no argument
    '''print('inclusive no argument call')
    for i in inclusive_range1():
        print(i, end=' ')'''
    print('inclusive one argument call')
    for i in inclusive_range1(25):
        print(i, end=' ')
    print()
    print('inclusive two argument call')
    for i in inclusive_range1(5, 25):
        print(i, end=' ')
    print()
    print('inclusive three argument call')
    for i in inclusive_range1(5, 25, 3):
        print(i, end=' ')
    # triggers TypeError for extra arguments
    '''print('inclusive more than three argument call')
    for i in inclusive_range1(5, 25, 3, 54):
        print(i, end=' ')'''

# generator func
def inclusive_range(start, stop, step):
    i = start
    while i <= stop:
        yield i # returns i, after the first execution will start executing right after yield statement
        i += step

def inclusive_range1(*args):
    numargs = len(args)
    if numargs < 1: 
        raise TypeError('requires at least one argument')
    elif numargs == 1:
        stop = args[0]
        start = 0
        step = 1
    elif numargs == 2:
        (start, stop) = args # because tuple
        step = 1
    elif numargs == 3:
        (start, stop, step) = args
    else: raise TypeError('inclusive_range1 expected at most 3 arguments, got {}'.format(numargs))
    i = start
    while i <= stop:
        yield i
        i += step

if __name__=="__main__": main()
