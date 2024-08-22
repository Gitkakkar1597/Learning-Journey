# Can you change the values inside a list which is contained in set S?



# No, because we can't even add a list to a set as lists are mutable/hashable.
# Example usage
s = {8,7,12,"Harry"}
print(type(s))                    # <class 'set'>

s.add([1,2])                      # TypeError: unhashable type: 'list' 