# Write a program to create a dictionary of hindi words with values as their English translation. 
# Provide user with an option to look it up!

words = {
    "Kya" : 'What',
    "Kyu" : 'Why',
    "Kaise" : 'How',
    "Kon" : 'Who',
    "Konsa" : "Which"
}

word = input("Enter the hindi word you want the translation of :  ")         # Kya

print(words[word])                                                           # What