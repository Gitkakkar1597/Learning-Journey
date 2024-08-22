# Methods in tuples python

# 1. count() : Return the number of occurences of an element in a tuple
'''
Syntax:-
tuple.count(element)
'''
tup = (34,"Sid",False,"Orange",82.29,True,False)
print(tup.count(False))      # 2


# 2. index() : Returns the index number of the first-occurence of an element in a tuple
'''
Syntax:-
tuple.index(element)
'''
tup1 = (19,32,3,35,53,24,43)
#        0  1 2  3  4  5  6
print(tup1.index(24))          # 5
# print(tup1.index(False))          # ValueError: tuple.index(x): x not in tuple


# Tuple operations

# 1. Length : Returns the length of the tuple using len() function
tup2 = (41,4,15,35,32,5,3,52,1,54)
print(len(tup2))         # 10

# 2. Concatenation : Tuples can be concatenated using (+) operator
tup3 = (1,2,3)
tup4 = (4,5,6,7)
tup5 = tup3 + tup4
print(tup5)        # (1, 2, 3, 4, 5, 6, 7)


# 3. Repitition: Tuples can be repitited using the (*) operator
tup6 = (10,20,30)
tup7 = tup6*3
print(tup7)           # (10, 20, 30, 10, 20, 30, 10, 20, 30)


# 4. Membership : Check if an element exists or not in a tuple using 'in' keyword
tup8 = (3,24,32,43,24,1)
print(10 in tup8)           # False
print(43 in tup8)           # True


# 5. Slicing: Tuples support slicing to form a new tuple from the subset of the original tuple
tup9 = (3,34,3,14,3,1,43,1)
tup10 = tup9[3:7]
print(tup10)           # (14, 3, 1, 43)


# 6. Unpacking : Tuples can be unpacked into individual variables
tup11 = (1,2,3)
a,b,c = tup11
print(a,b,c)                 # 1 2 3

