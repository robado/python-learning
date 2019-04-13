#! /usr/bin/python
# 5.1 Loops and Iterables

# loop

s = "hello worlds"
a = [4, 6, 9]
# in looks if that elements is in list and print True or False
print(5 in a)
print(4 in a)
print("ello" in s)

# for loop. iterating a list
for even_number in [2, 4, 6, 8, 10]:
    print(even_number)
    # in for loop you can add more and more code

odds = [1, 3, 5, 7, 9, 11]
for odd_number in odds:
    print(odd_number)

# Gets the length of a list and then print for every number the element
print(range(len(odds)))  # 0, 6
for index in range(len(odds)):
    print("Index: {:d}, odd number: {:d}".format(index, odds[index]))
