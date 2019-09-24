#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 17:45:40 2019

@author: Mehedi Hasan Akash
"""

class Duck:
	def __init__(self, **kwargs): # constructor, keyword arguments to store any number of inputs
		self.variables = kwargs # _variableName makes the variable local, using dictionary
	
	# object controller (set and get)
	def set_variables(self, k, v):
		self.variables[k] = v
	
	def get_variables(self, k):
		return self.variables.get(k, None)

def main():    
	#using dictionary
	donald = Duck(color = 'Gray')
	print(donald.get_variables('color'))
	print(donald.get_variables('feet'))
	
	kevin = Duck(feet = 2, color = 'black')
	print(kevin.get_variables('color'))
	print(kevin.get_variables('feet'))
	
	donald.set_variables('color', 'blue')
	print(donald.get_variables('color'))
	print(donald.get_variables('feet'))
	
	donald.set_variables('feet', 2)
	print(donald.get_variables('color'))
	print(donald.get_variables('feet'))

if __name__ == '__main__': main()
