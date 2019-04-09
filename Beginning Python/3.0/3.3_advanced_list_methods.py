#! /usr/bin/python
# 3.3 Advanced List Methods

alpha1 = ["a", "d", "f", "e"]
alpha2 = ["i", "h", "g"]
alpha3 = "jklmnopqrstuvxyzäöå"

# Sorting list
alpha1.sort()
alpha2.sort()
print(alpha1)
print(alpha2)

# Inser into list
alpha1.insert(1, "b")
alpha1.insert(2, "c")
print(alpha1)

# Converting list to string
# It takes every element from list and concats it
alpha1 = ''.join(alpha1)
alpha2 = ''.join(alpha2)
print(alpha1)
print(alpha2)

in_alphabet = alpha1 + alpha2 + alpha3
print(in_alphabet)