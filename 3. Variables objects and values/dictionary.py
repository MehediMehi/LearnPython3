#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 12:15:17 2019

@author: Mehedi Hasan Akash
"""

def main():
    d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
    print(type(d), d)
    for k in d:
        print(k, d[k])
    for k in sorted(d.keys()): # sorted in alphabetical order by keys
        print(k, d[k])
    # another method using dict class
    d = dict(
            one = 1, two = 2, three = 3, four = 4, five = 'five'
            )
    d['seven'] = 7
    print(type(d), d)
    

if __name__ == "__main__": main()