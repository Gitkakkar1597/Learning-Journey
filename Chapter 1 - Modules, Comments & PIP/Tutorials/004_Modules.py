# Modules in python

# A python module is like a toolbox filled with special tools (already wriiten-codes) 
# It can be imported in our python program

# For example, if we've to calculates harmomic mean of various numbers, we've to write a code from scratch
# But, with help of module, we can import ot & perform the task in much less line of code

# Using PIP (package manager for python), we can install a python module from terminal
# Example: Flask module for web-apps, django framework that is imported as paclage as well, etc
# Syntax : pip install module_name 

# Types of modules :- 1. Pre-installed (os, random) ; 2. Built-in (tensorflow, flask)

# Example usage (Pyjokes)
# pip install pyjokes

# Import module in program
import pyjokes

# store joke in a variable
joke = pyjokes.get_joke()

# print the joke
print(joke)

# Prints a new random joke everytime the progarm is executed
# Example : What do you mean 911 is only for emergencies? I've got a merge conflict.


