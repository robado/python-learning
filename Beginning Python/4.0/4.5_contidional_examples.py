#! /usr/bin/python
# 4.5 Conditional Examples

# First I try without watching the answer and then I also write the teachers answer.

# --------------------------------------------------
# Write a program that given two numbers a, b print "divisible"
# If one of the two numbers divides the other

print("Give first number: ")
number1 = int(input())
print("Give second number: ")
number2 = int(input())

if number1 % number2 == 0:
    print("The first number is divisible")
elif number2 % number1 == 0:
    print("The second number is divisible")

# Teacher
a, b = int(input("a = ")), int(input("b = "))
if a % b == 0 or b % a == 0:
    print("divisible")


# --------------------------------------------------
# Given input a, b print a/b if b is not equal to zero

a, b = int(input("a= ")), int(input("b= "))
if b != 0:
    print(a/b)

# Teahcer
a, b = int(input("a= ")), int(input("b= "))
if b != 0: print(a/b)
if b is not 0: print(a/b)
if not(b == 0): print(a/b)

# --------------------------------------------------
# Write a program that given three names prints "equal"
# if all three names are equal to each other when lowercase

name1 = str(input("Please enter your first name: ")).lower()
name2 = str(input("Please enter your middle name: ")).lower()
name3 = str(input("Please enter your last name: ")).lower()

if name1 == name2 == name3:
    print("equal")

# Tacher
name1 = input("name1: ")
name2 = input("name2: ")
name3 = input("name3: ")

if name1.lower() == name2.lower() == name3.lower():
    print("equals")