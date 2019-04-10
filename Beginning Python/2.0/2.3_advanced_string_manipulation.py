#! /usr/bin/python
# 2.3 Advanced String Manipulation

# concatination
prefix = "python is an "
suffix = "awesome language"

# Combines strings
astr = prefix + suffix
print(astr)

# Replace one word with another
astr = astr.replace("language", "banana.")
print(astr)

# Multiplies string
astr = astr * 2
print(astr)

astr = astr.replace("banana.", "language")
print(astr)

# Can set how many times replaces.
astr.replace("banana.", "language", 1)

# Count, it counts how many times occurs
print(astr.count("an"))