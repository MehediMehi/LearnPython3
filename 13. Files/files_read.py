#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 13:30:14 2019
@author: Mehedi Hasan Akash
Github: https://github.com/MehediMehi
"""
# open('fileName.extension', 'mode')

def main():
    f = open('lines.txt') # by default opens the file in the read mode if not specified ('r' = read, 'w' = write, 'a' = append, and other special ones ('r+', 'w+', 'a+', 'rb' = binary mode, 'rt' = text file mode))
    for line in f: # f = file handle object, iterable. (f.readlines() does the same thing)
        print(line, end='')

if __name__ == "__main__": main()