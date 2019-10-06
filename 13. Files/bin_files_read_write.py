#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 14:49:08 2019
@author: Mehedi Hasan Akash
Github: https://github.com/MehediMehi
"""
# buffered IO is needed for binary files as files are not listed or arranged as lines.
# Task: as read method is not iterable, you can write your own read method using generators (functions) which will be iterable. 

def main():
    buffersize = 50000 # read in buffered mode instead of line by line. 50000 bytes (your buffer can be any sized (depending on device and ram))
    infile = open('olives.jpg', 'rb') # read in binary mode
    outfile = open('new.jpg', 'wb') # write in binary mode
    buffer = infile.read(buffersize) # filling the buffer. buffer is now a binary object, not a text object at all
    while len(buffer): # while loop because read() method of file handle object is not iterable.
        outfile.write(buffer) # as long as buffer is not empty. writing buffer into outfile
        print('.', end='') # printing in the screen just to show the hits
        buffer = infile.read(buffersize) # reading again for changing the buffer data
    print()
    print('Done.') # feedback in the screen

if __name__ == "__main__": main()