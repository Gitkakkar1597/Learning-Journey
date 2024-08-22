# Type & Typecasting in python

# Since, there are various data types like none, int, float, etc
# To find the type of a variable, type() function is used

# Example usage
a = 10
print(type(a))          # <class 'int'>

b = 292.82
t = type(b)
print(t)                  # <class 'float'>

c = 'Siddharth'
t = type(c)
print(type(c))             # <class 'str'>


# Its great that we can print the data-type of a variable
# Whats even greater is that we can convert one datatype into another type
# But, ONLY when its VALID datatype



# Example usage
a = "92.28"

# b = a but b should be float
b = float(a)
print(b)                       # 92.28
print(type(b))                 # <class 'float'>

# 'float()' is a function and so are 'str()' and 'int()' provided conversion is LEGAL