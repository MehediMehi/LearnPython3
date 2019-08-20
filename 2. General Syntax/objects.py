#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 12:00:50 2019

@author: Mehedi Hasan Akash
"""
# self is the reference to the object itself

class Egg:
    def __init__(self, kind = "fried"):
        self.kind = kind # object variables are the reference to the object itself
        
    def whatKind(self):
        return self.kind

def main():
    fried = Egg()
    scrambled = Egg('scrambled')
    print(fried.whatKind())
    print(scrambled.whatKind())

if __name__ == "__main__": main()