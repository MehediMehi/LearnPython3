#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 17:00:10 2019

@author: Mehedi Hasan Akash
"""

class Duck:
	def __init__(self, value = "White Duck"): # constructor
		self._v = value # _variableName makes the variable local 
    
	def quack(self):
		print("Quaaack!", self._v)
    
	def walk(self):
		print("Walks like a duck.", self._v)
	# object controller (set and get)
	def set_value(self, value):
		self._v = value

	def get_value(self):
		return self._v

def main():
	frank = Duck() # value encaptulated into the object 
	frank.quack()
	frank.walk()

	junk = Duck() # value encaptulated into the object 
	junk._v = "Black Duck"
	junk.quack()
	junk.walk()
    
	donald = Duck("Gray Duck")
	donald.quack()
	donald.walk()

	print(donald.get_value()) # get the value
	donald.set_value("Blue Duck") # set the value
	print(donald.get_value())

if __name__ == '__main__': main()