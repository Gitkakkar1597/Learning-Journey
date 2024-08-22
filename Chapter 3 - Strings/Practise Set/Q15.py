# Replace the double space from previous problem with single spaces

str1 = "Siddharth is a very  good  good boy"

print(str1.replace("  "," "))         # Siddharth is a very good good boy

# Remember that python strings are immutable
# replace() doesn't affects original string
print(str1)                           # Siddharth is a very  good  good boy
