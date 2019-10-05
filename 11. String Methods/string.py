#!C:\Users\Mehedi Hasan Akash\Anaconda3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 10:54:04 2019
@author: Mehedi Hasan Akash
Github: https://github.com/MehediMehi
"""
# String is an object just like everything is an object in python
# In python a variable is just a reference to an object

print("This is a string")
s = "this is a string" # assigning in a variable
print(s)
print(s.upper()) # To make all uppercase *(does not change the main string which is in s)
print("this is a string".upper()) # Would do the same without assigning in a variable
print(s.capitalize()) # to make first character of a sentence capital *(does not change the main string which is in s)
su = "This had Upper CASE now lower"
print(su.lower()) # to make all lowercase *(does not change the main string which is in su)
sw = "This Is A Swapped String"
print(sw.swapcase()) # to swap cases (UPPER - lower / lower - UPPER) *(does not change the main string which is in sw)
print(s.find('is')) # to find the position of the match in the sentence (here first is in the word This, where i of is starts at the position 2 (0, 1, 2, 3...))
print(s.replace('this', 'that')) # to replace this by that (as string is immutable, it does not change the main string but creates another string to show the change)
print(s) # to see that main string did not change
sws = "     This is a string with white spaces in the beginning and also in the end     "
print(sws) # string with extra white spaces
print(sws.rstrip()) # rstrip() removes extra white spaces from the end
print(sws.strip()) # strip() removes extra white spaces (but commonly used for removing extra newlines (\n) in the end)
print("This is a string with new line\n")
print("This is a string with new line\n".strip()) # does not print extra new line which is in the string
print(s.rstrip('ing')) # removes anythin defined here from the end of the string if that is present
# Methods for testing the content of the string
print("This is a string".isalnum()) # Checks if all of the characters are alphaneumerical. Will return False because of spaces
print("ThisIsAString".isalnum()) # Will return True as all of the characters in the string is alphanumerical
print("ThisIsAString".isalpha()) # Checks for only alpha characters. Will return True as all of the characters in the string is alphabetical (A-Z, a-z or other alpha characters in other languages)
print("1234567".isdigit()) # Checks for only numerical characters. Will return True as all of the characters in the string is numerical
print(s.isprintable()) # Checks if the string is printable. Will return True as characters inside the string s is printable
# Print with string
print("This is a string {}".format(42)) # pushing other values in string to show using .format() method
print("This is a string %d" % 42) # this also prints string alongwith pushed value but this style is old and python3 is getting over % (parcent operator) over time.
a, b = 5, 42
print(a, b) # .format is only available is python 3, it's more powerful, more consistant syntax and a lot easier to use. (repr method looks for the type for you and places according to that, you don't need to remember data types)
print("this is {}, that is {}".format(a, b)) # format method allows to put placeholders in a string and replace those placeholders with values and return a new string
print("this is %d, that is %d" % (a, b)) # this was the way in python 2 with % (parcent) operator
# change orders
print("this is {}, that is {}".format(b, a)) # change position inside format method
print("this is {1}, that is {0}".format(a, b)) # change position inside string using format method's parameter's index number (0th, 1st, 2nd...)
print("this is {1}, that is {0}, this too is {1}".format(a, b)) # number represents the positional order in which the arguments are provided to format
print("this is {bob} and that is {fred}".format(bob = a, fred = b)) # you can assign here and use them in placeholders
d = dict( bob = a, fred = b )
print("this is {bob} and that is {fred}".format(**d)) # ** to refer to the dictionary
# 90% of times this is all you will be going to need, for more visit http://docs.python.org/py3k/library/string.html
# splitting and joining strings
s = 'this is a string of words'
print(s.split()) # splits the string and puts the string apart with words (by default it splits based on white spaces and folds (first puts all of the corrosponding spaces together and treats as one) the output)
print(" this          is     a      string".split()) # split ignores the white spaces no matter how many are there
print(s.split("i")) # as we've defined other splitter (i), this now splits based on definded one, in this case i but folding option is not available as it is only reserved for white spaces
words = s.split()
print(words) # split creates a list
for w in words: print(w) # words is iterable as list is
new = ':'.join(words) # join method joins the list in a string, inside '' single quotations you can define which will be joining term
print(new)
print(', '.join(words)) # joins using (, ) a comma along with a space
# others
s = 'this is a string'
new = s.center(80) # pusehes the string to the right so that it creates 80 characters long string and the text is in the middle or in other words it makes the string length of 80 characters and aligns that to the center, so the text stays in the center and both of the sides are filled up with white spaces to make the length 80 
print(new)
# please read through this link to discover more http://docs.python.org/py3k/library/stdtypes.html#string-methods