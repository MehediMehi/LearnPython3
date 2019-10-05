#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 17:30:00 2019
@author: Mehedi Hasan Akash
Github: https://github.com/MehediMehi
"""

# bytes & byte arrays are like tuples and lists, except instead of containing orbitary objects, bytes and byte arrays contains bites, mutable so can be changed
# an 8 bit word of a data can hold upto 256 different values
# often used for converting strings
# utf-8 --> first 0-127 character of this works just as like ASCII character does
# file got converted into utf-16, got unicode values for each of those fancy characters in the file

def main():
    fin = open('utf8.txt', 'r', encoding = 'utf_8') # telling the OS to ignore it's default encoding system and use utf-8 (read with utf-8 encoding)
    fout = open('utf8.html', 'w') # defining output file. html to open in the browser
    outbytes = bytearray() # bytearray is a mutable list of bytes
    for line in fin: # iterate through the file
        for c in line: # iterate thtough the line for char
            if ord(c) > 127: # ord() built in, gives integer equivalent of a character (0-127 is same as ASCII (normal ASCII range), leave them)
                outbytes += bytes('&#{:04d};'.format(ord(c)), encoding = "utf_8") # bytes object, immutable. xlm entities '&#0000;', encoding for bytes constructor
            else:
                outbytes.append(ord(c)) # appended to the outbytes
    outstr = str(outbytes, encoding = 'utf_8') # convert into a string using encoding utf-8
    print(outstr, file = fout) # print it to our out file
    print(outstr) # also print in the console screen
    print('done')
    
if __name__ == "__main__": main()