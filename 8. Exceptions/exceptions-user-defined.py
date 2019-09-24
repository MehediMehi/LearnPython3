#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 15:33:10 2019

@author: Mehedi Hasan Akash
"""

def main():
    try:
        for line in readfile('lines.txt'):
            print(line.strip())
    except IOError as e: # user defined error message for misspells
        print('could not read file:', e)
    except ValueError as e: # user defined error message for file type
        print("bad file name", e)

def readfile(filename): # function to open file and return lines
    if filename.endswith(".txt"): # check the filename 
        fh = open(filename)
        return fh.readlines()
    else:
        raise ValueError('Filename must end with .txt')
        # raise keyword to raise an excaption

if __name__ == "__main__": main()
