# Comments in python

# Synatx : # (Pound symbol)
# Toggle using Shortcut : Ctrl + /  (Control and Forwafrd-slash)

# Used when we want some line to NOt be executed and for just understand code
# Interpreter ignorez this line as part of this program

# Types :-

# 1. Single line comment

'''
2. 
Multi
line
comment
'''


# Example usage (We want to indicate a joke is being printed)
import pyjokes

joke = pyjokes.get_joke()

# Print joke on console
print(joke)                # O/P: If at first you don't succeed, call it version 1.0.




# Way-1 (without comments)
'''
joke = pyjokes.get_joke()

This prints a joke  # Syntax error
print(joke)
'''


'''
O/P:-
File "d:\Python Programming\Python Tutorials\Chapter 1 - Modules, Comments & PIP\006_Comments.py", line 25
    This prints a joke  # Syntax error
         ^^^^^^
SyntaxError: invalid syntax
'''




# Way-2 (without comments)
'''
import pyjokes
joke = pyjokes.get_joke()

print("Printing joke ...")         # Not good as it gets printed on console as well
print(joke) 
'''


'''
O/P:-
d:\Python Programming\Python Tutorials\Chapter 1 - Modules, Comments & PIP\006_Comments.py:29: SyntaxWarning: invalid escape sequence '\P'
Printing joke ...
There are 10 types of people: those who understand hexadecimal and 15 others.
'''