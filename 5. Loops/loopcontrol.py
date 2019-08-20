#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 19:05:14 2019

@author: Mehedi Hasan Akash
"""

def main():
    s = 'this is a string'
    for i in s:
        print(i, end='')
    print()
    for i in s:
        if i == 's': continue
        print(i, end='')
    print()
    for i in s:
        if i == 's': break
        print(i, end='')
    print()
    for i in s:
        print(i, end='')
    else:
        print('\nelse')
    print()
    i = 0
    while(i < len(s)):
        print(s[i], end='')
        i += 1
    else:
        print('\nelse')

if __name__ == "__main__": main()