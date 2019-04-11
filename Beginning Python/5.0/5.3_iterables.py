#! /usr/bin/python
# 5.3 Iterables

# What is an iterable

list = [1,2,3,4,5]
tuple = (6,7,8,9,10) # Imutable
str = "Hello World"

# Check if the object is has iter in it
print('__iter__' in dir(list))
print('__iter__' in dir(tuple))
print('__iter__' in dir(str))
# Can take the element and print it or use it
# for elem in list:
    # print(elem)

# When using iterator the while loop will give an error because after the list ends it cannot print anything.
# This error must be catched! It is done with 'try'
list_iterator = iter(list)

while True:
    try:
        next_elem = next(list_iterator)
        print(next_elem)
    except StopIteration:
        break
