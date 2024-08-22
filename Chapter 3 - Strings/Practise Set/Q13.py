# Write a program fill in a letter template given below with name and date.

# letter = '''
#        Dear <|Name|>
#        You are selected!
#        <|Date|>
#         '''

# from datetime import date
# Name = input("Enter name: ")
# Date = str(date.today())

# letter = '''
#        Dear <|Name|>
#        You are selected!
#        <|Date|>
#         '''
        
# letter = letter.replace("<|Name|>",Name)
# letter = letter.replace("<|Date|>",Date)
# print(letter)
'''
Enter name: Siddharth

       Dear Siddharth   
       You are selected!
       2024-08-10    
'''


# NOTE: Efficient way
letter = '''
       Dear <|Name|>
       You are selected!
       <|Date|>
        '''
        
print(letter.replace("<|Name|>","John").replace("<|Date|>","10-08-2024"))
'''
       Dear John        
       You are selected!
       10-08-2024   
'''

# Here, the string after replacing 'Name' is then replaced where 'Date' is replaced
# Chaining of the function is carried-out here