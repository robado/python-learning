#! /usr/bin/python
# 2.5 User Input

# firstname, M. lastname

# This will ask an input from user
# This can be casted to string with str().
first_name = str(input("Please enter your first name: "))
middle_name = str(input("Please enter your middle name: "))
last_name = str(input("Please enter your last name: "))

# Capitalize (not mandatory)
first_name = first_name.capitalize()
middle_name = middle_name.capitalize()
last_name = last_name.capitalize()

# Using format
# in the "middle" I am taking only the first char
# I added a dot after middle so it will be a char and a dot
name_format = "{first} {middle:.1s}. {last}"
print(name_format.format(first=first_name, middle=middle_name, last=last_name))
