#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 15:13:30 2019

@author: Mehedi Hasan Akash
"""

def main():
    try:
        fh = open('lines.txt')
    except IOError as e:
        print("could not open the file!", e)
    else:
        for line in fh:
            print(line.strip()) # strip works as same as end=''
    
    # another way to use 
    try:
        fh = open('lines.txt')
        for line in fh: print(line.strip())
    except:
        print("could not open the file")

if __name__ == "__main__": main()