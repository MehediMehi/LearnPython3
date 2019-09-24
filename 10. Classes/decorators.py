#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 13:46:09 2019
@author: Mehedi Hasan Akash
Github: https://github.com/MehediMehi
"""
# Decorators: They can fundamentaly change the behavior of a function, here function methods operating as setter, getter, deleter. 
# But not calling them like functions, calling them in the normal proparty syntax. That's the power of decorators.  

class Duck:
    def __init__(self, **kwargs):
        self.properties = kwargs
        
    def quack(self):
        print("Quaaack!")
    
    def walk(self):
        print("Walks like a duck.")
        
    def get_properties(self):
        return self.properties
    
    def get_property(self, key):
        return self.properties.get(key, None)
    
    # Decorators
    @property # turns color() into an accessor for variable called color 
    def color(self): # accessor method works like getter method
        return self.properties.get('color', None)
    
    @color.setter # setter method for color
    def color(self, c):
        self.properties['color'] = c
    
    @color.deleter # delete method for color
    def color(self):
        del self.properties['color']
    
    
def main():
    # donald = Duck(color = 'blue') # don't need to initialize in this way anymore as we have decorators
    donald = Duck()
    donald.color = 'blue'
    # print(donald.get_property('color')) # don't need to get the value in this way either
    print(donald.color) # using decorators
    
if __name__ == "__main__": main()