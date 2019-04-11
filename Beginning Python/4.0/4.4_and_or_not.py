#! /usr/bin/python
# 4.4 'And', 'OR', and 'NOT'

# So logical thinking in Python is kinda cool. It checks that is the statement true or false. Few examples below.
T = True
F = False

statement1 = 3 > 4  # False
statement2 = 10 % 5 == 0  # True
statement3 = "A".lower() == "a"  # True
print(statement1, statement2, statement3)

# False isn't printing.
# OR
if F or F: print("F or F")
if F or T: print("F or T")
if T or F: print("T or F")
if T or T: print("T or T")
print("")
# AND
if F and F: print("F or F")
if F and T: print("F or T")
if T and F: print("T or F")
if T and T: print("T or T")
print("")

# NOT
# not(3 == 6) 3 != 6
print(not (3 == 6))
print(not (3 != 6))
if not F: print("not F")
if not T: print("not T")

# This was interesting, I didn't quite understand myself how the logic works, but the main point is I think that if it
# something is false it doesn't get executed (or printed) and if true it executes.
