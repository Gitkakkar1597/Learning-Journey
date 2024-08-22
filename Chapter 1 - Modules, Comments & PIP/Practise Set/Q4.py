# Write a python program to print the contents of a directory using the os module. Search online for the function which does that

import os

path = "D:/"
contents = os.listdir(path)

for item in contents:
    print(item)