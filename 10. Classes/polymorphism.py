#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 12:54:11 2019

@author: Mehedi Hasan Akash
"""

''' Polymorphism and Method Overriding
In literal sense, Polymorphism means the ability to take various forms. 
In Python, Polymorphism allows us to define methods in the child class 
with the same name as defined in their parent class. '''

# in the case of multi-level inheritances, a Python super() will always refer the immediate superclass.

class Duck():
	def quack(self):
		print('Quaaack!')
	def walk(self):
		print('Walks like a duck.')
	def bark(self): # overriding
		print('The duck cannot bark.')
	def fur(self): # overriding
		print('The duck has feathers.')

class Dog():
	def bark(self):
		print('Woof!')
	def fur(self):
		print('The dog has brown and white fur.')
	def walk(self): # overriding
		print('Walks like a dog.')
	def quack(self): # overriding
		print('The dog cannot quack.')

def main():
	donald = Duck()
	donald.quack()
	donald.walk()
	fido = Dog()
	fido.bark()
	fido.fur()
	
	for o in (donald, fido):
		o.quack()
		o.walk()
		o.bark()
		o.fur()
	
	# objects in python don't actually care what the name of the class is.
	# duck typing (loosly typed)
	''' Duck typing in computer programming is an application of the duck test—"If it walks like a duck and it quacks like a duck,
	then it must be a duck"—to determine if an object can be used for a particular purpose.
	With normal typing, suitability is determined by an object's type. '''
	
	in_the_forest(donald) # providing duck while expecting dog
	in_the_pond(fido) # prividing dog while expecting duck

def in_the_forest(expecting_dog): # any objects that impliments those methods (bark, fur) will work, no matter what class that belongs
	expecting_dog.bark()
	expecting_dog.fur()

def in_the_pond(expecting_duck): # any objects that impliments those methods (quack, walk) will work, no matter what class that belongs
	expecting_duck.quack()
	expecting_duck.walk()

if __name__ == '__main__': main()
