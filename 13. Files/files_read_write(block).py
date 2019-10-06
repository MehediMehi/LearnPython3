#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 13:45:39 2019
@author: Mehedi Hasan Akash
Github: https://github.com/MehediMehi
"""
# read or write part of the file, not one line after line

def main():
    buffersize = 50000 # read in buffered mode instead of line by line. 50000 bytes (your buffer can be any sized (depending on device and ram))
    infile = open('bigfile.txt', 'r')
    outfile = open('new.txt', 'w') # creates file if not exist and writes into
    buffer = infile.read(buffersize) # filling the buffer. 
    while len(buffer): # while loop because read() method of file handle object is not iterable. 
        outfile.write(buffer) # as long as buffer is not empty. writing buffer into outfile
        print('.', end='') # printing in the screen just to show the hits
        buffer = infile.read(buffersize) # reading again for changing the buffer data
    print()
    print("Done.") # feedback in the screen

if __name__ == "__main__": main()