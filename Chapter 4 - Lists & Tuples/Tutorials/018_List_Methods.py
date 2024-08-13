# Lists methods in python

# Just like in strings, there are various methods for lists operations & manipulation
# But unlike in strings where a new string was printed, here changes are made in the list itself

# Example usage

# 1. append() : Inserts an element at the end of a list
'''
Syntax:-
list.append(element)
'''
friends = ["Akash", "Orange", 5, 245.06, False, "Apple", "Rohan"]
print(friends)                    # ['Akash', 'Orange', 5, 245.06, False, 'Apple', 'Rohan']
friends.append(True)
print(friends)         # ['Akash', 'Orange', 5, 245.06, False, 'Apple', 'Rohan', True]



# 2. sort() : Sorts a list in ascending/descending order
'''
Syntax:-
list.sort()
'''
l1 = [324,54,1255,542,24,523,32,4,43]
l1.sort()
print(l1)              # [4, 24, 32, 43, 54, 324, 523, 542, 1255]


# 3. reverse() : Reverses a list
'''
Syntax:-
list.reverse()
'''
l2 = [9,8,7,6,5,4,3,2,1]
l2.reverse() 
print(l2)           # [1, 2, 3, 4, 5, 6, 7, 8, 9]



# 4. insert() : Inserts an element at a specified index from LHS in the list & simultaneously shifts rest of the list elements to RHS by one
'''
Syntax:-
list.insert(index,element)
'''
l3 = [19,291,187,831,19]
#      0  1   2   3   4
l3.insert(2,818)                # Inserts '808' at index '2'
print(l3)                # [19, 291, 818, 187, 831, 19]



# 5. pop() : Removes the element at a particular index from a list & returns the value(element at that index)
'''
Syntax:-
list.pop(index)
'''
l4 = [823,5,34245,4354,3245,21]
print(l4.pop(3))          # Removes element at index '3' , here it's '4354'
print(l4)                 # [823, 5, 34245, 3245, 21]



# 6. remove() : Removes a particular element from the list
'''
Syntax:-
list.remove(element)
'''
l5 = [138,3241,53321,4,24,554,42]
l5.remove(53321)
print(l5)              # [138, 3241, 4, 24, 554, 42]