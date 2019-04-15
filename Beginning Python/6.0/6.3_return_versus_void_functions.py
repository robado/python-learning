#! /usr/bin/python
# 6.3. Return Versus Void Functions

def is_even(number):
    # Tests to see if number is multiple of 2
    if number % 2 == 0:
        # Returns True and exists functions
        return True

    # number was odd, return False
    return False


print(is_even(int(input())))

print("I return nothing, I just print things to the console")


def is_even_without_return(number):
    # Tests to see if number is multiple of 2
    if number % 2 == 0:

        # number was even, display to console
        print("{:d} is even".format(number))

    else:

        # number was odd, display to console
        print("{:d} is odd".format(number))


# So when I call the function it just prints the text based on what the function is doing
is_even_without_return(6)
