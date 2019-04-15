#! /usr/bin/python
# 6.7 Recursion Examples

# So this first one counts recursively vowels in a string.
def count_vowels(s, i=0):
    # This checks does it have any characters to check if zero it returns zero
    if (i == len(s)): return 0

    # This is the main part of this method. So first it is a part of vowels it return the vowel and then it
    # increments the index to see the next character. If it finds a vowel it adds one. I didn't 100% understand how
    # this works but I see what is the logic in this one Basically how I understood this is that it sees if it is a
    # vowel or not and if yes then it continues and increments the number
    c = s[i]
    if c in 'aeiou':
        # Has a vowel
        return count_vowels(s, i + 1) + 1
    # not have found a vowel
    return count_vowels(s, i + 1) + 0


print(count_vowels('hello'))
print(count_vowels('aeiou'))


# 345 -> 3+4+5 = 12
# 345 / 10 = 34 / = 3 / 0 = 0
# This next one I liked quite a bit. So this takes a string of numbers and sums them and how it does it is quite simple
# but fun. So firstly it checks that is it zero or not because if zero it just returns zero. Otherwise it divides it by
# 10. The logic in here is that it chops the number and when the number is chopped it gets the right most number.
# It continues this as long as it reaches zero
def digit_sum(n):
    if n == 0: return 0
    return digit_sum(n // 10) + n % 10


print(digit_sum(345))
print(digit_sum(666))


# Was too late in the evening to type my explanation to this... will do it as soon as I have time!
# 0 1 2 3 4 5 6 ...
# 1 1 2 3 5 8 13 ...
def fib(n):
    if n == 0 or n == 1: return 1
    return fib(n - 2) + fib(n - 1)


for i in range(10):
    print(fib(i))
