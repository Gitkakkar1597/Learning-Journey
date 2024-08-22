# Sets methods in python


# 1. len() : Returns the length of the set
'''
Syntax:-
len(set)
'''
s = {1,8,2,3,6,8,3,7}
print(s)                          # {1, 2, 3, 6, 7, 8}
print(len(s))                     # 6



# 2. remove() : Removes an element fromt he set & updates the set
'''
Syntax:-
set.remove(element)
'''
s.remove(2)
print(s)                          # {1, 3, 6, 7, 8}



# 3. pop() : Removes an arbitrary element from the set & returns the element removed ; Not preferred as it removes random elements from the set collection
'''
Syntax:-
set.pop()             
'''
print(s.pop())                     # 1
print(s)                           # {3, 6, 7, 8}



# 4. clear() : Removes all elements of the set (Empties it)
'''
Syntax:-
set.clear()
'''
s.clear()
print(s)                           # set()       




# 5. add() : Inserts an element in the set
'''
set.add(element)
'''
s1 = {72,93,28,82,82,27,48,74}
s1.add(99)
print(s1, type(s1))                             # {48, 82, 99, 72, 74, 27, 28, 93} <class 'set'>

# NOTE: No effect of add() method if the element to be added already exists in the set
s1.add(48)
print(s1)                                       # {48, 82, 99, 72, 74, 27, 28, 93}



# 6. union() : Returns a new set containing elements from two sets
'''
Syntax:-
set1.union(set2)
'''
s3 = {7,4,48,47,58}
s4 = {47,4,8,5,85}

print(s3.union(s4))                         # {4, 5, 7, 8, 47, 48, 85, 58}



# 7. intersection() : Returns a new set containing elements that are common in both the sets
'''
Syntax:-
set1.intersection(set2)
'''
print(s3.intersection(s4))                      # {4, 47}  



# 8. difference() : Returns all those elements of set1 that are not in set2
'''
Syntax:-
set1.difference(set2)
'''
print(s3.difference(s4))                          # {48, 58, 7}



# 9. issubset : Returns True or False that whether a set2 is a subset of set1; A set is a subset if it's elements exists in/ belongs to another set
'''
Syntax:-
set1.issubset(set2)
'''
set1 = {1,2,3,4,5}
set2 = {1,5,3}

print(set2.issubset(set1))                         # True



# 10. issuperset : Returns True or False that whether a set1 is a superset of set2; A set is a superset if it has elements (and other than elements) that exists in/ belongs to another set(subset)
'''
Syntax:-
set1.issuperset(set2)
'''
set1 = {1,2,3,4,5}
set2 = {1,5,3}

print(set1.issuperset(set2))                        # True







