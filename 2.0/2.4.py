# 2.4 String formatting

n = 11
f = 1.23456789
s = "banana"

''' d is for decimal and base 10. {} are 
    for format. b is for printing in binary '''
print("This is the number {:d}".format(n))
print("This is the number {:b}".format(n))

# Some Format types:
# e - exponents
# b - binary (base 2)
# o - octal (base 8)
# d - decimal (base 10)
# x - hexadecimal (base 16)
# f - floats (decimal numbers)
# s - strings (default if none is specified)

# float
print("This is float {:f}".format(f))
# Print only last 3 number (plus it rounds the number)
print("This is float {:.3f}".format(f))
# First number is how many characters I want and the second is how many after decimal point
print("This is float {:11.3f}".format(f))
# 0 adds zeroes
print("This is float {:011.3f}".format(f))

# Multiple formats
print("{0} {1} {2}".format(n,f,s))

# Specific names for formatter
print("{name} own(s) {amount} of {object}".format(
    name = "John",
    amount = 666,
    object = "BANANAS"
))