#! /usr/bin/python
# 3.2 List Methods

# Append. Adding to list
alpha = ["a", "b", "c", "d"]
alpha.append("e")
alpha = alpha + ["f"]
print(alpha)

# Removing element
# Getting the index of an element from list
# Then removing it
d_index = alpha.index("d")
print("d_index: " + str(d_index))
del alpha[d_index]
print(alpha)

# Simpler way
alpha.remove("a")
print(alpha)