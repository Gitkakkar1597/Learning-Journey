# Slicing in strings python

# A string in python can be sliced for getting a part of the string

# Being immutable, characters in already existing string can't be changed/replaced with another character(s)
# Strings are indexed, i.e., numbered from starting(first) characetr till last character in a sequence starting from 0 till (length-1)
# Indexing : 0,1,2,3,..

# Indexing can be negative as well when indexings tarts from alst towards first character , i.e., -1,-2,-3,..


# Example usage

name = "Siddharth"

# Length of a string: Number of characters inside that string
# Calculated using len() function that accepts string variable as an argument

length = len(name)
print("Length of name : ", length)

# Syntax for slicing string:-
# sliced_string = string[starting_index : ending_index]

# Note that ending_index isn't included

short_name = name[0:3]            # Return character sequence starting from 0 all the way till 3 , exclusing the 3rd character
print(short_name)        # Sid

char1 = name[1]
print(char1)


# Negative Slicing
Name = "Siddharth"

# For negative slicing, convert to corresponding positive indices
print(Name[-4:-1])      # art

# Is as same as :-
print(Name[5:8])        # art


# Advanced slicing techniques

# string_variable[:i] means from 0th index to ith index (character at i^th is excluded)
# Similarly, string_var[4:] means from 4th indexx to the (length-1) index

print(Name[1:])       # iddharth
print(Name[:6])       # Siddha
print(Name[:])        # Siddharth



# Slicing With A Skip-Value

# Defines how much characters are skipped/JUMPED TO during slicing within defined slicing range
# Example, if skip value = 2, means jump to 2nd character from character at current index
# Syntax:-
# skipped_sliced_string = string_variable[start_idx : stop_idx : skip_value]

# Exampel usage
str1 = "Amazing"
print("String: ", str1)                               # Amazing
print("Sliced string : ", str1[1:6])                  # mazin
print("Sliced string with skip = 2: ", str1[1:6:2])   # mzn
print("Sliced string with skip = 3: ", str1[1:6:3])   # mi


# REPL Example 

'''
PS D:\Python Programming\Python Tutorials> python
Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> a = "0123456789"
>>> a[1:9]
'12345678'
>>> a[1:9:2]
'1357'
>>> a[1:9:3]
'147'
>>> a[1:9:1]
'12345678'
>>> a[1:9:0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: slice step cannot be zero
>>>
'''
