# Dictionary in python

# Just like in lists & tuples, dictioanries are used to store collection of data
# Here, data is stored in key-values pairs

# Example usage
dict_ = {}                # Empty dictionary
dict1 = {
    "Key" : "Value",
    "Sid" : "Codes",
    "Marks" : 82,
    "List" : [23,34,13]
}

print(dict1["Key"])        # Value
print(dict1["List"])       # [23, 34, 13]





# Example: Store marks and name key-value pairs when marks are mapped to their names
marks = {
    "John" : 81,
    "Kathy" : 28,
    "Clark" : 92,
    "Oliver" : 72,
    "Lois" : 85
}

print(marks, type(marks))
# {'John': 81, 'Kathy': 28, 'Clark': 92, 'Oliver': 72, 'Lois': 85} <class 'dict'>

# NOTE: Dictionaries can also be thought of as List of key-value pairs where 'keys' are associated with 'values' 


# We can't access key/value using indexing liek in lists & tuples
# print(marks[0])             # KeyError: 0


# We can use the keys itself to access corresponding values
print(marks["John"])      # 81

# Usage of dictionary
# When there are 1000 or more like huge number of rows/key-value pairs of data
# In that scenario, accessing value using 'key' acts as a LOOKUP which is very efficient , like time-complexity of search is O(1)

# We could also have used nested lists for this , but that would've been computationally-expensive operation
marks = [["Harry",100],["Siddharth",92]]
# We couldn't have accessed marks or 'value' using "Harry" or 'key' essentially



# Properties of python dictionaries
# 1. Unordered (Order doesn't matter here)
# 2. Mutable (Dtaa can be changed/mofified like values of already existing associated-keys can be changed.It changes the original dictiionary itself like in Lists )
# 3. Indexed (Lookups value directly using 'keys'. Doesn't look for value one-by-one like in numbered-indexing)
# 4. Cannot contain duplicate keys

