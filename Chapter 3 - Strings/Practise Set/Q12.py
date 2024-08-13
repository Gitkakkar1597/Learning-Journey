# write a python program to display a user entered name followed by Good Afternoon using input() function

# name = input("Enter your name : ")
# print("Good afternoon \"",name,"\"")
'''
Enter your name : Siddharth
Good afternoon " Siddharth "
'''


# NOTE : Use f-strings
# Syntax:-
# f"string_content {variable}"

name = input("Enter name: ")
print(f"Good afternoon {name}")
'''
Enter name: Siddharth
Good afternoon Siddharth
'''

# Earlier, format function or string concatenation was used
Name = "John"
print("Hello, my name is "+Name+"!")          # Hello, my name is John!
