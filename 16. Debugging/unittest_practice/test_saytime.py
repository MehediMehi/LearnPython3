#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:17:40 2019
@author: Mehedi Hasan Akash
Github: https://github.com/MehediMehi
"""
'''The unittest package's main() will actually open up this file and parse it and
   find the classes that import unittest (here TestSaytime), and it will go ahead
   and run the test in that class.'''
# There are a lot to explore!
# unittest documentation link: https://docs.python.org/3/library/unittest.html

import saytime # this is the module we are working on
import unittest # this is the unittest framework from the Python standard library

class TestSaytime(unittest.TestCase):
    def setUp(self): # to do any initialization 
        self.nums = list(range(11)) # list of numbers (0 to 10)
    
    def test_numbers(self):
        # make sure the numbers translate correctly
        words = (
            'oh', 'one', 'two', 'three', 'four', 'five',
            'six', 'seven', 'eight', 'nine', 'ten'
        ) # expected results of saywords numwords (saytime.py)
        for i, n in enumerate(self.nums): # index and the number
            self.assertEqual(saytime.numwords(n).numwords(), words[i]) # assertEqual method from the unittest package, compare two values, if not equal will throw an AssertionError 
    
    def test_time(self):
        time_tuples = (
            (0, 0), (0, 1), (11, 0), (12, 0), (13, 0), (12, 29), (12, 30),
            (12, 31), (12, 15), (12, 30), (12, 45), (11, 59), (23, 15), 
            (23, 59), (12, 59), (13, 59), (1, 60), (24, 0)
        ) # times that are testing
        time_words = (
            "midnight",
            "one past midnight",
            "eleven o'clock",
            "noon",
            "one o'clock",
            "twenty-nine past noon",
            "half past noon",
            "twenty-nine til one",
            "quarter past noon",
            "half past noon",
            "quarter til one",
            "one til noon",
            "quarter past eleven",
            "one til midnight",
            "one til one",
            "one til two",
            "OOR",
            "OOR"
        ) # expected results (saytime.py)
        for i, t in enumerate(time_tuples):
            self.assertEqual(saytime.saytime(*t).words(), time_words[i]) # assertEqual method from the unittest package, compare two values, if not equal will throw an AssertionError 

if __name__ == "__main__": unittest.main() # calling unittest's main() instead of saytime's main()