# Sets in python

# Well-defined collection of data with non-repitition

# Example usage
# Syntax for sets in python:-
set1 = {37,91,18}
print(set1)                     # {18, 91, 37}
print(type(set1))               # <class 'set'> 

# Empty set declaration
e = set()
print(e)                        # set()
# NOTE: Don't use e ={} as it's an empty dictionary, not an empty set

# Sets are used where data shouldn't contain repitition of elements/values
s = {1,2,2,3,3,3,4,4,4,4,5,5,5,5,5}
print(type(s))                  # <class 'set'>  
print(s)                        # {1, 2, 3, 4, 5}

# Observe that order isn't maintained; use lists for ordered collection
s1 = {7,9,6,2,5,2,8,3,6,2,7,3,2,6,3,2,6,7,4,3}
print(s1)                       # {2, 3, 4, 5, 6, 7, 8, 9}

# Sets can store different data types as well
s2 = {81,83.27,True,"Sid",False,True,81,"Siddharth"}
print(s2, type(s2))             # {False, 'Sid', True, 'Siddharth', 81, 83.27} <class 'set'>




# Properties of sets
'''
1. Sets are unordered : Elements' order doesn't matter
2. There's no way to change (existing) items in sets : Sets are already well-defined collection of objects
3. Sets CANNOT contain duplicate values
4. Sets are unindexed : Elements of a set cannot be accessed by index
'''


