#! /usr/bin/python
# 6.6 Recursion

# Function calling itself
# Doubles the number n
# double(2) -> 4
# double(15) -> 30
def double(n):
    # base case
    if n == 0:
        return 0

    # recursive call
    return double(n - 1) + 2


print(double(3))  # prints 6


# So how did I understand this recursive. Basically the math for this one looks like ((((0) + 2) + 2) + 2) = 6. When
# I call double(3), first it checks that it isn't zero and then if not it minuses 1 from the number and then adds 2
# so now we are calling +2. And it does this for the numbers of time until it reaches zero. After that it sums the
# number so 2+2+2=6.

def exponentiate(b, e):
    # Base case
    if (e == 0): return 1

    # recursive call
    return exponentiate(b, e - 1) * b


print(exponentiate(2, 3))  # prints 8
# So this time it does the same but this can recursively compute (b^e)
