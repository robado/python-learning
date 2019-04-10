#! /usr/bin/python
# 3.4 Built-in List Functions

# List manipulation
number = [3.14, 2, 4, -64, 23, 34**4]
hello_world = "HelloWorld"

# min, max, sum, len
# number.min() # method on list
print(min(number)) # function
print(max(number))
print(sum(number))
print(len(number))

# function with strings
# First max() sorts capital letters and
# lower case letters
# min() does the opposite
# Cannot sum str but can get length
print(max(hello_world)) # I get r
print(min(hello_world)) # I get H
#print(sum(hello_world)) # Error
print(len(hello_world)) # 10
