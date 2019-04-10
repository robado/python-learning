#! /usr/bin/python
# 3.6 List Slicing

# List slicing can query a part of list
a = list(range(0, 10))
print(a)

# SLICING
# This prints first 5 elements
print(a[0:5])
# all the elements from index onwards
print(a[2:len(a)])
# Simpler length
print(a[2:])

# Every single letter. "step"
# With first and second it can be controlled from what you want to start.
print(a[::2])
# for example I start from 0 to 6 and every 2nd element
print(a[0:6:2])

# Gives last element of array. Negative numbers start from the end.
print(a[-1])
# This is from 2 to 8
print(a[2:-2])
# Reversing array???
print(a[::-1])
# Reverses and gets every 2nd element
print(a[::-2])
