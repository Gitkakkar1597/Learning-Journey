# Set union & intersection in python

# Union
# Returns a new set containing elements from two sets
'''
Syntax:-
set1.union(set2)
'''
s3 = {7,4,48,47,58}
s4 = {47,4,8,5,85}

print(s3.union(s4))                # {4, 5, 7, 8, 47, 48, 85, 58}



# Intersection
# Returns a new set containing elements that are common in both the sets
'''
Syntax:-
set1.intersection(set2)
'''
print(s3.intersection(s4))        # {4, 47}  


# Operations

# 1. Set1 - Set2
# Returns all those elements of set1 that are not in set2
print(s3-s4)

print(s3.difference(s4))