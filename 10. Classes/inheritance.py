#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 12:10:33 2019

@author: Mehedi Hasan Akash
"""
# in the case of multi-level inheritances, a Python super() will always refer the immediate superclass.

class Animal:
	def talk(self): print('I have something to say!')
	def walk(self): print("Hey! I'm walkin' here!")
	def clothes(self): print('I have nice clothes.')

class Duck(Animal): # Duck is inheriting Animal
	def quack(self):
		print('Quaaack!')
	
	def walk(self):
		super().walk() # accessing parent walk method using super (immediate parent class)
		print('Walks like a duck.') # uses chield class walk method (override)

class Dog(Animal):
	def clothes(self):
		print('I have brown and white fur') # overriding clothes method

def main():
	donald = Duck()
	donald.quack()
	donald.walk()
	donald.clothes()
	
	fido = Dog()
	fido.walk()
	fido.clothes()

if __name__ == '__main__': main() 
