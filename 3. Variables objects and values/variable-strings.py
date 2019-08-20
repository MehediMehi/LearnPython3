#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 19:59:19 2019

@author: Mehedi Hasan Akash
"""

def main():
    s = "This is a string!"
    print(s)
    s = 'This is a string!'
    print(s)
    s = "This is a \nstring!"
    print(s)
    s = r"This is a \nstring!" # r for raw string
    print(s)
    n = 32
    s = "This is a {} string!".format(n)
    print(s)
    s = '''This is a string!
with multiple lines'''
    print(s)
    s = """This is a string!
with multiple lines"""
    print(s)

if __name__ == "__main__": main()