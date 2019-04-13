#! /usr/bin/python
# 5.5 Prime Number Checker

# n = int(input("n = ")) So I dont have to run program over and over. This could have also been made in while mode
# where it asks me an input until I stop the program
for n in range(-10, 10):
    if n >= 2:
        divisors = []
        for divisor in range(2, n):
            if n % divisor == 0:
                divisors.append(divisor)

        if len(divisors) == 0:  # prime!
            print("{:d} is prime".format(n))
        else:
            print("{:d} is not prime because {:} divide {:d}".format(n, str(divisors), n))
    else:
        print("{:d} is not prime!".format(n))
