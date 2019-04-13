#! /usr/bin/python
# 3.5 2D Arrays and Array References

# 2D matrixes
# import the pprint function from the pprint module as a function called pretty_print
from pprint import pprint as pretty_print
# imports the copy and deepcopy functions from the copy module
from copy import copy, deepcopy

# array of arrays. Array contains arrays
nums_2d = [
    [1, 2, 3, 4, 5, 6, 7],
    [8, 9, 10, 11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20, 21, 22]
]
# This is the way how to query 2D arrays. First query row x and then the placement of the element
print(nums_2d[1][3])  # prints 11

# Hard to read because all in one line
print(nums_2d)
# Makes reading easier
pretty_print(nums_2d)

# Changing value
nums_2d[2][1] = -666
pretty_print(nums_2d)  # 17 is now -666

letters = ["A", "B", "C", "D", "E"]
letters_2d = [letters, letters, letters]
pretty_print(letters_2d)
letters_2d[0][0] = "F"
pretty_print(letters_2d)  # Changed every A to F. This happened because "letters" is a list and that list is inside
# 2D list. So when it references the list inside 2D list, it references the original list hence changing all the values
# inside the 2D list.

# Use the imported "copy" to copy individually lists into 2D list. Now every row is unique
letters_2 = ["A", "B", "C", "D", "E"]
letters_2d_2 = [copy(letters_2), copy(letters_2), copy(letters_2)]
letters_2d_2[0][0] = "F"
pretty_print(letters_2d_2)
