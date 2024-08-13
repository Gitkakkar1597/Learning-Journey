# Label the program written in problem 4 with comments

# Importing neceassry modules
import os

# Store path of main directory
path = "D:/"

# Store contents
contents = os.listdir(path)

# Print each file int he directory one by one
for item in contents:
    print(item)