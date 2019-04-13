#! /usr/bin/python
# 5.4 Loops and Conditionals

# Here are two programs that uses loops and conditions

# 2nd program
# This program checks that is the number equals and then prints the total
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
total = 0
for n in numbers:
    if n % 2 == 0:
        # total = total + n
        # This is shorter way and is commonly used
        total += n
    # I had mu print here so it printed every number in the loop. I had my spacing wring, but if I wanted to see
    # every number printed, I would put this printing here print(total)
print(total)

# 1st program
# This program extracts all the consonants from a string. Basically this program checks from alpha what characters
# there are and if it is not a vowel (which as defined) and then adds all the consonants to a list and then the list is
# printed
alpha = 'abcdefghijklmnopqrstuvwxyuzABSCDEFGHIJKLMNOPQRSTUVWXYUZ'
vowels = 'aeiouAEIOU'
my_string = "Bananas and orages rocks!"

characters = []
for char in my_string:
    if char not in vowels and char in alpha:
        characters.append(char)
consonants = ''.join(characters)
print(consonants)
