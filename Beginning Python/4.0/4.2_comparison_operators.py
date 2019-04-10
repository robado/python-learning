#! /usr/bin/python
# -*- coding: utf-8 -*-
# 4.2 Comparison Operators

# Different types of operators
# ==, !=, <, >, >=, <=
tmp = """
(-∞ -30]   REALLY COLD!
(-30, 0)    Cold
0           Zero
(0, 20)     Chilly
[20, 40)    Hot
[40, ∞)     THIS IS HELL!"""
print(tmp)

# Getting user input as int
print("")
print("How cold is it? ")
t = int(input())
# Here I am setting the statements that if it is this much so print this.
if (t <= -30):
    print("REALLY COLD!")
if (t < 0):
    if(t > -30):
        print("Cold")
if (t == 0):
    print("Zero")
if (t > 0):
    if (t < 20):
        print("Cilly")
if (t >= 20):
    if(t < 40):
        print("Hot")
if (t >= 40):
    print("THIS IS HELL!")



