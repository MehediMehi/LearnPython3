#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:23:38 2019
@author: Mehedi Hasan Akash
Github: https://github.com/MehediMehi
"""
# import modules and use them (about python standard libraries & PyPI - Python Package Index)
# look through this documentation to know about available python standard libraries. Link: http://docs.python.org/py3k/library
# look through this documentation to know about available third party modules( Python Package Index). Link: http://pypi.python.org/pypi
# You don't need to reinvent the wheel when that is available already.

import sys # System-specific parameters and functions http://docs.python.org/py3k/library/sys.html

def main():
    print("Python version {}.{}.{}".format(*sys.version_info)) # get python version
    print("Operating System plartform: {}".format(sys.platform)) # OS category plartform 
    
    import os # can import a module inside any class or function
    
    print("OS name: {}".format(os.name)) # get os name
    print("Environment variable: {}".format(os.getenv('PATH'))) # environment variables from the os
    print("Current working directory: {}".format(os.getcwd())) # Current working directory
    print("Urandom funcion: {}".format(os.urandom(25))) # gives string of random bytes (here 25 bytes long) with byte type
    
    import urllib.request
    
    page = urllib.request.urlopen('http://google.com/') # grab a webpage from the internet
    print("Page: {}".format(page)) # iterable object
    for line in page: print(str(line, encoding = 'utf_8'), end = '') # convert each line in a string as they come as binary
    print()
    
    import random
    
    print("Random number: {}".format(random.randint(1,1000))) # generate a random number between 1 and 1000
    x = list(range(25)) # create the list of 25 numbers (0 - 24)
    print("List: {}".format(x)) # show the list
    random.shuffle(x) # shuffle the list x using random.shuffle() method
    print("Shuffled list: {}".format(x)) # Show shuffled list
    random.shuffle(x) # shuffle the list x using random.shuffle() method again
    print("Shuffled list: {}".format(x)) # Show shuffled list
    
    import datetime
    
    now = datetime.datetime.now()
    print("Current date & time:{}".format(now)) # show current date time 
    print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond) # can access any of them depending on needs
    
    # Using PyPI libraries
    import bitstring # installation link: https://pypi.org/project/bitstring/
    
    a = bitstring.BitString(bin = '01010101')
    print(a.hex, a.bin, a.uint) # print in different number system

if __name__ == "__main__": main()