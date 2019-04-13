#! /usr/bin/python
# 4.1 Control Flow

# Check age with if statement
age = 666
# == is for checks for equality
# Indentation is IMPORTANT!
if age == 666:
    print("Age is equal to 666")

# With str
# If first if statement is false so the second if statement wont execute
name = "Optimus"
if name == "Optimus":
    print("My name is " + name + " Prime")
    if age == 666:
        print("My name is " + name + " Prime and I am " + str(age) + " years ols")
