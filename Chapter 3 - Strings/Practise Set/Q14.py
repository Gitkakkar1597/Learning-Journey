# Write a program to detect double space in string

# str1 = input("Enter a string:")
# if "  " in str1:
#     print("Double spaces detected!")
# else:
#     print("No double spaces in the string")
    
'''
Enter a string:My name is   Siddharth
Double spaces detected!
'''


# Use find()
str1 = "Siddharth is a very  good  good boy"
print(str1.find("  "))                      # 19 (The first index of the occurence)