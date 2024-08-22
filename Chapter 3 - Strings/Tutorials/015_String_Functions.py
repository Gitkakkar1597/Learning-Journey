# String functions in python

# To perform operations / manipulations on strings
# Here are some major string functions in python



# 1. len() : Returns length of the string
'''
Syntax:-
len(string_variable)
'''
name = "Siddharth"
print(len(name))     # 9

# 2. endswith() : Returns 'True' if a string ends-with a particular character-sequence/string
'''
Syntax:-
string_variable.endswith(string_to_be_checked)
'''
print(name.endswith("rth"))         # True
print(name.endswith("art"))         # False
# NOTE: Functions are case-sensitive

# 3. startswith() : Returns 'True' if a string starts with a particular characters/string
'''
Syntax:-
string_variable.startswith(string_to_be_checked)
'''
print(name.startswith("sid"))       # False
print(name.startswith("Sid"))       # True

# 4. capitalize() : Capitalizes first character/alphabet of the string/sentence
'''
Syntax:-
string_variable.capitalize()
'''
str1 = "my name is X"
print(str1.capitalize())          # My name is X

# 5. count() : Returns the number of occurences of a character in a string
'''
Syntax:-
string_variable.count(character_to_be_counted)
'''
print(name.count("d"))            # 2

# 6. str() : Type-conversion(Converts an object into a string)
'''
Syntax:-
str(object)
'''
var = 123
print(type(var))          # <class 'int'>
print(type(str(var)))     # <class 'str'>

# 7. find() : Finds a word (string) & returns the index of first occurence of that word in the string
'''
Syntax:-
string_variable.find(word)
'''
str2 = "Hello world"
print(str2.find("world"))         # 6

# 8. replace() : Replaces the 'old word' with a 'new word' for all occureneces of the 'old word' in the entire string
'''
Syntax:-
string_variable.replace(old word, new word)
'''
print(str2.replace("world","World!"))            # Hello World!

'''
PS D:\Python Programming\Python Tutorials> python
Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> a = "Siddharth is a very good good boy"
>>> a.replace("good","bad")
'Siddharth is a very bad bad boy'
>>> 
'''
