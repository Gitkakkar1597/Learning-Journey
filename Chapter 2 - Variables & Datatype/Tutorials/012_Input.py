# User input in python

# Use 'input()' function

# Example usage : User input to sum two numbers

a = input("Enter number 1 : ")
b = input("Enter number 2 : ")

print("Number 1 : ", a)         # 91
print("Number 2 : ", b)         # 18

print("Sum : ", a+b)               # Sum :  9118
    
'''
What happened here is:-
'a' and 'b' inputs were in string type inputs
That's why on suming, the strings got 'concatenated'
Input type should've been int type for addition of numbers

REPL Example to understand this :-
>>> 'Sid' + 'codes'
'Sidcodes'
>>> '19' + '72'
'1972'
>>> 19 + 72
91  
'''

# Type conversion needed here

a = int(input("Enter number 1 : "))
b = int(input("Enter number 2 : "))

print("Number 1 : ", a)                # 91
print("Number 2 : ", b)                # 19

print("Sum : ", a+b)                   # 110