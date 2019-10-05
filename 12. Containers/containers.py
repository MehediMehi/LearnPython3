#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 15:55:52 2019
@author: Mehedi Hasan Akash
Github: https://github.com/MehediMehi
"""
# tuples and lists are the basic array type in python, tuples are immeutable and lists are mutable
# Why would you need a tuple then?
""" Tuples are there because more often thean not when you need them you dont need to be changing them.
It's a smaller class, it's simpler to impliment and they are faster for some things 
but most importantly they don't allow you to change stuffs.
So when you need values not to be changed accidently, use tuple instead of list."""

# tuple
t = 1,2,3,4,5 # parenthesis is for binding, it's not necessary, but comma (,) is necessary to create a tuple
test = (1) # parenthesis does not make this tuple
test1 = (1,) # comma (,) does
print(type(test)) # test is an integer
print(type(test1)) # test1 is a tuple with one element
print(t)
print(type(t)) # t is a tuple too
print(t[0]) # beginning of the tuple
print(t[4]) # end of the tuple
print(t[-1]) # end of the tuple
print(len(t)) # length of the tuple
print(min(t)) # smallest element of the tuple
print(max(t)) # largest element of the tuple

# list
x = [1,2,3,4,5] # braces [] and comma (,) both are needed to create a list
print(x)
print(type(x))
print(x[0]) # beginning of the list
print(x[4]) # end of the list
print(x[-1]) # end of the list
print(len(x)) # length of the list
print(min(x)) # smallest element of the list
print(max(x)) # largest element of the list

# immutable tuple
t = tuple(range(25)) # create a 25 length tuple with 0 to 24 numerical values
print(t)
print(type(t))
print(t[10]) # show the 10th index value
#t[10] = 42 # will catch an error as tuple can not be changed
print(t[10])

# mutable list
x = list(range(25)) # create a 25 length list with 0 to 24 numerical values
print(x)
print(type(x))
print(x[10]) # show the 10th index value
x[10] = 42 # will not catch an error as list can be changed
print(x[10])
print(x)

#operations
# any operation can be done on tuple that does not need to modify the tuple
t = tuple(range(25))
print(t)
print(type(t))
print(10 in t) # searches 10 in t and replies either True if found or False
print(50 in t)
print(50 not in t) 
print(t[10])
print(len(t))
for i in t: print(i) # tuple is iterable
x = list(range(25))
print(x)
print(type(x))
print(10 in x) # searches 10 in t and replies either True if found or False
print(50 in x)
print(50 not in x) 
print(x[10])
print(len(x))
for i in x: print(i) # list is iterable

# t[10] = 25 # won't execute as tuple is immutable
x[10] = 25 # will execute as list is mutable
print(t)
print(x)
print(t.count(5)) # count method to count how many 5s are there in the tuple
print(x.count(5)) # count method to count how many 5s are there in the list
print(t.index(5)) # will return the index of the element 5
print(x.index(5)) # will return the index of the element 5
# t.append(100) # can not append because it's a tuple which is immutable
x.append(100)
print(x) # 100 has been appended at the end of x
print(len(x)) # length is extended because added one element at the end of the list (effects the main list)
x.extend(range(20)) # it will extend the list with twenty more elements from 0 to 19. Append can't do this operation
print(x)
x.insert(0, 25) # insert(position, value)
print(x)
x.insert(12, 200) # insert(position, value)
print(x)
x.remove(12) # looks for the element with the value 12 and removes if found (removes one that is found first, not all the 12s)
print(x)
del x[12] # this will delete the element at the index 12
print(x)
print(x.pop()) # returns the last index element and also removes from the list
print(x)
print(x.pop(0)) # returns the index element mentioned in the argument list and also removes from the list
print(x)