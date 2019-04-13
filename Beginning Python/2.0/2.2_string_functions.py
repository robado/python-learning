#! /usr/bin/python
# 2.2 String Functions
# Lection 2.2 of Beginning Python

science = "SCIENCE"
apple = "apple"
banana = "BANANA"

'''String methods for python API 
https://docs.python.org/3/library/stdtypes.html#string-methods'''

# apple variable before upper
print(apple)
apple = apple.upper()
# and after
print(apple)

# science variable lowercased
print(science.lower())
# science variable title, so first letter is capitalized
print(science.title())

'''.strip removes trailing characters and then
    uppercased the word '''
banana = "               banana                                       "
banana = banana.strip().upper()
print(banana)
