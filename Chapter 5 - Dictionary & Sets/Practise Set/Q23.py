# Write a program to input eight numbers from the user & display all the unique numbers (once)


# Declare an empty set as set stores unique numbers
e = set()

# Store 8 numbers one by one
num = input("Enter a number: ")             # 9
e.add(int(num))

num = input("Enter a number: ")             # 3
e.add(int(num))

num = input("Enter a number: ")             # 1
e.add(int(num))

num = input("Enter a number: ")             # 1
e.add(int(num))

num = input("Enter a number: ")             # 5
e.add(int(num))

num = input("Enter a number: ")             # 1
e.add(int(num))

num = input("Enter a number: ")             # 8
e.add(int(num))

num = input("Enter a number: ")             # 1
e.add(int(num))

# NOTE that number is converted to int type to be added to the set

# Print unique numbers
print(f"Unique numbers : {e}")                   # Unique numbers : {1, 3, 5, 8, 9}