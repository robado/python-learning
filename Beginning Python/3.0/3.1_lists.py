#! /usr/bin/python
# 3.1 Lists

# List of number
numbers = [1, 2, 3, 4, 5, 6, 4, 7]
# List of strings
# I can but number into list of strings
names_str = ["John", "Mary", "Dick"]

# Use index to get values.
# List starts from 0 (zero)
print(names_str[0]) # John
print(names_str[1]) # Mary
print(names_str[2]) # Dick
# print(names_str[3]) # IndexError

# Deleting elements
print(names_str)
del names_str[1] # Mary
print(names_str)

# Similarities
mystr = "Hello World"
# Querying string
print(mystr[0])
print(mystr[6])

# Strings are immutable
# Can't change string
# del mystr[2]