# Create an empty dictionary. 
# Allow four friends to enter their favourite language as value and use key as their names.
# Assume that the names are unique




# Create empty dictionary
dict1 = {}

# Enter keys & values
name = input("Enter friend's name : ")               # Siddharth
lang = input("Enter language name: ")                 # Python
dict1.update({name : lang})

name = input("Enter friend's name : ")               # Priyanshu
lang = input("Enter language name: ")                 # Java
dict1.update({name : lang})

name = input("Enter friend's name : ")               # Hardik
lang = input("Enter language name: ")                 # JavaScript
dict1.update({name : lang})

name = input("Enter friend's name : ")               # Shorya
lang = input("Enter language name: ")                 # C++
dict1.update({name : lang})



print(dict1)                               # {'Siddharth': 'Python', 'Priyanshu': 'Java', 'Hardik': 'JavaScript', 'Shorya': 'C++'}