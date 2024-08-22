# Escape sequence characters in python

# Special sequance of characters after a backslash ('\')
# NOTE: They may comprise of more than one characters but they REPRESENT one character when used within strings
# Example usage
 
 
# 1. '\n' - New line character

# Suppose you want to print something in a new line

# Throws an error
'''
a = "Sid is a very
good boy"

    a = "Harry is a very
        ^
SyntaxError: unterminated string literal (detected at line 8)

'''

# So, we use "\n" here as a special escape sequence character
# It is manipulated inside the string as a new line

a = "Sid is a very\ngood boy"
print(a)
'''
Sid is a very
good boy   
'''



# 2. '\t' - Tab character

str1 = "Value of a+b:\t1027"
print(str1)                     # Value of a+b:   1027



# 3. \" : Double quotes chracater

# Do not use double quotes literally inside the string
# This throws error

'''
str2 = "My name is "Siddharth" "
print(str2)

str2 = "My name is "Siddharth" "
                        ^^^^^^^^^
SyntaxError: invalid syntax
'''

# Use \" escape sequence

str2 = "My name is \"Siddharth\" "
print(str2)                # My name is "Siddharth"


# NOTE: Use single-quote escape sequence (\') if the string is defined using single-quotes
# Otherwise, '' isnide a string defiend using "" is okay

str3 = "My self 'John' "
print(str3)                 # My name is 'Kathy'

'''
str4 = 'My name is 'Kathy''
print(str4)

str4 = 'My name is 'Kathy''
                        ^^^^^  
SyntaxError: invalid syntax 
'''

str4 = 'My name is \'Kathy\' '
print(str4)                      # My name is 'Kathy'




# 4. \\ - Backslash character

# When you want to print a backslash(\) inside a string

line = "Use backslash (\\) for escape sequences in python"
print(line)                       # Use backslash (\) for escape sequences in python

