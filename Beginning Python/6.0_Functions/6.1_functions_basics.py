#! /usr/bin/python
# 6.1 Functions Basics

PI = 3.1415592

# Area of a circle
print(5 * 5 * PI)
print(10 * 10 * PI)
print(13 * 13 * PI)


# etc......

# Functions can make this count for me. With functions I don't have to do a similar code over and over again. With
# function I can write the code once and if I want to do the same stuff I can use the function I just created.
def circle_area(r):  # Function name
    return PI * r * r


print(circle_area(5))
print(circle_area(10))
print(circle_area(13))

# Here I can see that I didn't have to write the code three times, I just called it and it did the job. Also this
# makes the code look more cleaner.
