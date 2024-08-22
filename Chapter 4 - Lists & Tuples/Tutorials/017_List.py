# Lists in python

# To store multiple elements of one type, lists/tuples or ararys are used in programming languages
# In python, lists are used

# Python lists are a container to store a set of values of any data type
# Syntax:-
# list_name = [element1, element2,..]

# Example usage
friends = ["Akash", "Orange", 5, 245.06, False, "Apple", "Rohan"]
print(friends)            # ['Akash', 'Orange', 5, 245.06, False, 'Apple', 'Rohan']

# LIST INDEXING
print(friends[0])         # Akash

# A list can be indexed, just like strings
# But, lists are mutable, unline strings which were immutable

'''
>>> a = "sid"
>>> a[0]
's' 
>>> a[1] = 'w'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>>
'''

# Change list elements
friends[0] = "Grapes"
print(friends[0])           # Grapes

# Lists are flexible and mutable
# Elements can be added/removed


# LIST SLICING
# Lists can be sliced just like in strings using indices

print(friends[1:5])           # ['Orange', 5, 245.06, False]
