#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 17:02:55 2019
@author: Mehedi Hasan Akash
Github: https://github.com/MehediMehi
"""
# dictionaries --> associated arrays or hashed arrays
# for tuples and lists, indexes are always numeric. In case of the dictionary, indexes are data 
# dictionaries within dictionaries --> possible
# lists or/and tuples within dictionaries --> possible

# create
d = { 'one': 1, 'two': 2, 'three': 3 } # { 'keyValue': value,}
print(d)
print(type(d))
d = dict(one = 1, two = 2, three = 3) # uses constractor, easier way, gives the same result
print(d)
print(type(d))
x = dict( four = 4, five = 5, six = 6 ) # dict(keyValue = value,)
print(x)
print(type(x))
d = dict(one = 1, two = 2, three = 3, **x) # appending an other dictionary while creating one (two astarics ** are used in this case)
print(d)
print(type(d))
print('four' in x) # True if found the key
print('three' in x) # False because three keyword is not present in the dictionary x
for k in d: print(k) # dictionary is iterable, in this case, only keys will be printed
for k, v in d.items(): print(k, v) # Keys along with values will be printed
print(d['three']) # prints the value for the key 'three'. Problem is that if your dictionary does not have that key it will get an exception (error)
print(x.get('three')) # get method solves exception, gives None value if not found instead of exception (error)
print(d.get('three')) # if found, returns the value corrosponding to that key
print(x.get('three', 'not found!')) # prints user defined default value if not found instead of None
del x['four'] # deletes the value and key if matches
print(x)
print(x.pop('five')) # returns the value which matches with the key and delets both key and value then
print(x)
