# If names of two friends are same, what will happen to the program in problem previously ?




# Since we used update() method, previous value gets updated with the new one for the same key

# Create empty dictionary
dict1 = {}

# Enter keys & values
name = input("Enter friend's name : ")               # Siddharth
lang = input("Enter language name: ")                 # Python
dict1.update({name : lang})

name = input("Enter friend's name : ")               # Priyanshu
lang = input("Enter language name: ")                 # JavaScript
dict1.update({name : lang})

name = input("Enter friend's name : ")               # Priyanshu
lang = input("Enter language name: ")                 # Java
dict1.update({name : lang})

name = input("Enter friend's name : ")               # Shorya
lang = input("Enter language name: ")                 # C++
dict1.update({name : lang})


print(dict1)                               # {'Siddharth': 'Python', 'Priyanshu': 'Java', 'Shorya': 'C++'}

