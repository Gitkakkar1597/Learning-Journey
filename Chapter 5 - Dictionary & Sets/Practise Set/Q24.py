# Can we have a set with 18(int) and "18"(str) as a value in it

# Yes it is poosible

# Declare empty set
s = set()

# Store values
s.add(18)
s.add("18")

print(type(s), s)                 # <class 'set'> {18, '18'}