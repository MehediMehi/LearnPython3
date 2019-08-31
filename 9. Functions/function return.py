#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:46:40 2019

@author: Mehedi Hasan Akash
"""

def main():
    print(testfunc())
    for n in testfunc1(): print(n, end=' ')

def testfunc():
    return 42

def testfunc1():
    return range(25)

if __name__=="__main__": main()
