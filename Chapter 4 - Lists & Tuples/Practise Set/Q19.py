# Check that a tuple cannot be changed in python

a = (64,864,"Sid")

a[2] = "Harry"
'''
a[2] = "Harry"
    ~^^^
TypeError: 'tuple' object does not support item assignment
'''
