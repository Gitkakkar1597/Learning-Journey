# Dictionary methods/in-built functions in python

# Example usage
# Consider the following dictionary
marks = {
    "John" : 81,
    "Kathy" : 28,
    "Clark" : 92,
    "Oliver" : 72,
    "Lois" : 85
}


# 1. items() : Returns a list of (key , value) tuples
'''
Syntax:-
dictionary.items()
'''
print(marks.items())            # dict_items([('John', 81), ('Kathy', 28), ('Clark', 92), ('Oliver', 72), ('Lois', 85)])



# 2. keys() : Returns a list containing dictionary's keys
'''
Syntax:-
dictionary.keys()
'''
print(marks.keys())             # dict_keys(['John', 'Kathy', 'Clark', 'Oliver', 'Lois'])



# 3. values() : Returns a list containing dictionary's values
'''
Syntax:-
dictionary.values()
'''
print(marks.values())           # dict_values([81, 28, 92, 72, 85])



# 4. update() : Update the dictionary with supplied key-value pairs
'''
Syntax:-
dictionary.update({key:value})
'''
marks.update({"John" : 28})       # Proof of mutability of python dictionary
print(marks)                    # {'John': 28, 'Kathy': 28, 'Clark': 92, 'Oliver': 72, 'Lois': 85}

# NOTE : Key-values pairs which doesnt exist will be added in the dictionary passed in the method
marks.update({"Oliver":72,"Lex":98})
print(marks)                    # {'John': 28, 'Kathy': 28, 'Clark': 92, 'Oliver': 72, 'Lois': 85, 'Lex': 98}



# 5. get() : Returns the value of specified key( and value is returned)
'''
Syntax:-
dictionary.get(key)
'''
print(marks.get('Lana'))        # None
print(marks.get('Clark'))       # 92

# NOTE: marks.get("Clark") differs against marks["Clark"] when the key doeesn't exist in the dictionary
# marks.get(key') prints "None" while marks[key'] returns an Error when key doesn't exists, otherwise the output is same



# 6. copy() : Returns a shallow copy of the dictionary
'''
Syntax:-
dictiionary.copy()
'''
markz = marks.copy()
print(markz)                    # {'John': 28, 'Kathy': 28, 'Clark': 92, 'Oliver': 72, 'Lois': 85, 'Lex': 98}



# 7. clear() : Removes all elements from the dictionary
'''
Syntax:-
dictionary.clear()
'''
markz.clear()
print(markz)                    # {}



# 8. fromkeys() : Create a new dictionary, with keys from 'seq' & values set to 'Value'
'''
Syntax:-
dictionary.fromkeys(key,value)
'''
keys = ['a','b','c']
new_dict = dict.fromkeys(keys,0)
print(new_dict)                # {'a': 0, 'b': 0, 'c': 0}



# 9. pop() : Removes a specified key from the dictionary; If key isn't found, returns Keyerror, or Default if provided
''' 
Syntax:-
dictionary.pop(key, default)
'''
marks.pop('John')
print(marks)                  # {'Kathy': 28, 'Clark': 92, 'Oliver': 72, 'Lois': 85, 'Lex': 98}

# marks.pop('Evalyn')                # KeyError: 'Evalyn'

print(marks.pop('Snyder', 'default_value'))       # default_value



# 10. popitem() : Removes & returns a (key,value) pair as a 2-tuple from the dictionary. Pairs are returned in LIFO order
''' 
dictionary.popitem()
'''
item = marks.popitem()
print(item)                          # ('Lex', 98)
print(marks)                         # {'Kathy': 28, 'Clark': 92, 'Oliver': 72, 'Lois': 85}



# 11. len() : Returns length of the dictionary (number of key-value pairs)
'''
Syntax:-
len(dictionary)
'''
print(len(marks))                   # 4

