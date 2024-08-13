# Tuples in python

# Immutable data type in python
# List in mustable ; Tuple isn't
# It is a collection of data and immutable; different from strings

# Example usage
a = (34,34,214,432,23)
print(type(a))           # <class 'tuple'>

# Empty tuple
tup = ()
print(tup)         # ()
print(type(tup))   # <class 'tuple'>


# NOTE : one-element tuple can't be defined with just using one element directly
tup1 = (1)
print(type(tup1))      # <class 'int'>
# Interpreter recognzes as an integer

# Correct way to define an one-element tuple
tup2 = (1,)
print(type(tup2))          # <class 'tuple'>
# Here, python interpreter recognizes that it's a collection with only one element


# Just like lists, python tuples can store different data types in one collection
tup3 = (34, "Karan", 93.128, True)
print(type(tup3))        # <class 'tuple'>
print(tup3)              # (34, 'Karan', 93.128, True)

# Accessing tuple elements
# Use indexing just like in strings/lists

tup4 = (9,124,"Sid",False,932.32,True,"Orange")
print(tup4[0])        # 9
print(tup4[1])        # 124
print(tup4[5])        # True


# Tuples are immutable
tup4[0] = 81         # TypeError: 'tuple' object does not support item assignment
