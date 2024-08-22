'''
What will be the length of the following set S:
s = Set()
s.add(20)
s.add(20.0)
s.add('20')   # length of s after these operations
'''

s = set()
s.add(20)             
s.add(20.0)
s.add('20')

# Length of the set should be 2 as three unique elements are added of different data types
print(type(s))              # <class 'set'>
print(s)                    # {20, '20'}
print(len(s))               # 2

for element in s:
    print(type(element))
    
'''
<class 'int'>
<class 'str'>
'''

# Float 20.0 wasn't added ; WHY??
# This happened because in python 1==1.0 is TRUE as python equality operator checks numerical equality, not data types
# That's why 20 == 20.0 & sets can't store duplicates