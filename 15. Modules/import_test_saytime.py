#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 16:25:32 2019
@author: Mehedi Hasan Akash
Github: https://github.com/MehediMehi
"""

import time, saytime # import time to grab the time as a local time variable, saytime to use our custom module propatries 

t = time.localtime() # grabbing the time as a local time variable
print("Content-type: text/html\n")
print(
    "In your location, it is now " +
    saytime.saytime_t(t).words() +
    time.strftime(', on %A, %d %B %Y.') # formatting the date and time
)

