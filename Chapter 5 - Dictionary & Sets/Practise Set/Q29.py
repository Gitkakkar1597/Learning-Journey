# If languages of two friends are same, what will happen to the program in problem previously ?




# Since, we used dictionary itself, rather than storing separate sets for names & languages 
# there would be no problem in previous program
# Dictionaries allow identical values as keys are identifiers, not the values

# Create empty dictionary
dict1 = {}

# Enter keys & values
name = input("Enter friend's name : ")               # Siddharth
lang = input("Enter language name: ")                 # Python
dict1.update({name : lang})

name = input("Enter friend's name : ")               # Priyanshu
lang = input("Enter language name: ")                 # Python
dict1.update({name : lang})

name = input("Enter friend's name : ")               # Hardik
lang = input("Enter language name: ")                 # JavaScript
dict1.update({name : lang})

name = input("Enter friend's name : ")               # Shorya
lang = input("Enter language name: ")                 # C++
dict1.update({name : lang})




print(dict1)                               # {'Siddharth': 'Python', 'Priyanshu': 'Python', 'Hardik': 'JavaScript', 'Shorya': 'C++'}