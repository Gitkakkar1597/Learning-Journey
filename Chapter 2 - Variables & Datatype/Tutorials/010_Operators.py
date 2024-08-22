# Operators in python

# Types :-
'''
1. Arithmetic operators: +,-,*,/
2. Assignment operators: =,+=,-=
3. Comparison operators: ==,>=,<=,<,>,!=
4. Logical operators: and,or,not
'''



# ARITHMETIC OPERATORS
a=1
b=5
c=a+b
print(c)
# 'a' & 'b' are 'Operands', '+' is 'Operator' & 'c' is the Result of operation



# ASSIGNMENT OPERATORS
a = 4-2       # '=' operator assigns '4-2' to variable 'a'
print(a)

b=6
b += 3        # '+=' operator increments the value of variable 'b' by 3 & then assigns value to the variable
print(b)
b *= 3
print(b)
b /= 3
print(b)



# COMPARISON OPERATORS
# Return value is always boolean, i.e., True/False

d = 5<4      # '<' operator checks if left operand is 'less than' right operand or not
print(d)

d = 5>=5     # '<=' operator checks if left operand is 'greater than or equal to' right operand or not
print(d) 

d = 8!=7     # '!=' checks if left operand is 'NOT EQUAL' to right oeprand or not
print(d)

d = 92==92     # '==' checks if left oepand 'is equal' to right operand or not
print(d)



# LOGICAL OPERATORS

e = True or False
print(e)                # 'True' as atleast one is true in 'or'

e = True and False
print(e)                # 'False' as one of them is false in 'and'

# Truth Table

# OR
print("True or True : ", True or True)
print("True or False : ", True or False)
print("False or True : ", False or True)
print("False or False : ", False or False)

# AND
print("True and True : ", True and True)
print("True and False : ", True and False)
print("False and True : ", False and True)
print("False and False : ", False and False)

# 'not' operator works only on ONE OEPRAND
# It converts True to False and vice-versa

print(not(True))                 # False