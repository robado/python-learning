#! /usr/bin/python
# 6.2 Parameters and Arguments

import datetime as dt


def add(a, b, c):
    return a + b + c


print(add(1, 2, 3))


# Takes unlimited numbers
# And in the functio goes through the numbers and counts them
def add_numbers(*numbers):
    total = 0
    for n in numbers:
        total += n
        return total


print(add_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9))


# In this function default parameter (time)
# Default parameters can be overwritten
def record_time(message, time=dt.datetime.now()):
    # can be saved to a file
    print("{:}, time: {:}".format(message, time))


record_time("It is morning")
record_time("It is morning", "Feb 22nd, 1998")
