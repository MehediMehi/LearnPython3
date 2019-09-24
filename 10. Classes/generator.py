#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 12:40:42 2019
@author: Mehedi Hasan Akash
Github: https://github.com/MehediMehi
"""
# yield works as return but has some difference and makes the function a generator.
# For yield, returns the value and from the next time when the function is called, starts executing right after the yield insted of starting from the beginning of the function body. 
# So the process is when the function is called for the first time, it will execute from the very beginning, initialize i, start while loop, check stop with i, return i using yield, but will not increment i.
# Next time when the function will be called, instead of starting from the beginning it will start executing right after the yield statement. So will increment i, check i with stop, return i with yield.
# And from the second call till wlile is false, this process will continue. 

# range(start=0, stop, step=1) which is noninclusive

# creating customized range which will be inclusive
class inclusive_range:
    def __init__(self, *args): # constractor (*args takes a list of arguments)
        numargs = len(args)
        if numargs < 1: raise TypeError('requires at least one argument')
        elif numargs == 1: # that must be stop
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif numargs == 2: # those must be start and stop
            (self.start, self.stop) = args
            self.step = 1
        elif numargs == 3: # those must be start, stop and step
            (self.start, self.stop, self.step) = args
        else: raise TypeError('expected at most 3 arguments, got {}'.format(numargs))
    
    def __iter__(self): # __iter__ makes the object an iterable object, gets called automatically (No need to use like object.__iter__() )
        i = self.start # starting point
        while i <= self.stop:
            yield i # for yield, returns the value and from the next time when the function is called, starts executing right after the yield insted of starting from the beginning of the function body.
            i += self.step

def main():
    o = range(25) # range is noninclusive. it will start at 0 and stop at 24, 25 is not included
    for i in o: print(i, end=' ')
    print()
    o1 = range(5, 25) # starting from 5, passing 1 step (default) for each iteration, stops at 24
    for i in o1: print(i, end=' ')
    print()
    o2 = range(5, 25, 2) # starting from 5, passing 2 steps for each iteration, stops at 23
    for i in o2: print(i, end=' ')
    print()
    print('Using custom range:') # inclusive
    o3 = inclusive_range(25) # starting from 0 (default), passing 1 step for (default) each iteration, stops at 25
    for i in o3: print(i, end=' ')
    print()
    o4 = inclusive_range(5, 25) # starting from 5, passing 1 step (default) for each iteration, stops at 25
    for i in o4: print(i, end=' ')
    print()
    o5 = inclusive_range(5, 25, 2) # starting from 5, passing 2 steps for each iteration, stops at 25
    for i in o5: print(i, end=' ')
    print()
    # no need to call __iter__() function by object.__iter__() 
    for i in inclusive_range(30): print(i, end=' ')
    # for no argument or more than 3 arguments it will raise error message
    """
    o6 = inclusive_range() # No argument given
    for i in o6: print(i, end=' ')
    print()
    o7 = inclusive_range(5, 25, 2, 7) # more than 3 arguments are given
    for i in o7: print(i, end=' ')
    print()
    """
    
if __name__ == "__main__": main()