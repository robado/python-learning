#! /usr/bin/python
# 4.3 Else and Elif

# else is executed if the if statement isn't true.
name = "Jebus"
if name == "Mercury":
    print("Mercury")
else:
    print("Name was not Mercury")

# elif can be used as many times as you want. So elif checks the condition until it reaches true or till the end.
if name == "Sarah":
    print("Emily")
elif name == "Mike":
    print("Mike")
elif name == "Bob":
    print("Bob")
else:
    print("Neither name was correct")

if name == "Sarah":
    print("Emily")

if name == "Mike":
    print("Mike")

if name == "Bob":
    print("Bob")

n = 6
if n < 20:
    print("n < 20 ")
elif n < 40:
    print("n < 40")
elif n < 60:
    print("n < 60")
else:
    print("n >= 60")

# Not much I can say about else and elif, I have used the same conditions in Java so this is quite familiar to me so
# don't know how could I explain this more clearer. But basically if the first statement is false elif checks the next
# one. If it is true it stops the program or until it reaches the end.
