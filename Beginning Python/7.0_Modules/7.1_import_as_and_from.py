#! /usr/bin/python
# 7.1 'import', 'as' and 'from'

# Some usage of imports
# Importing math. After importing it is ready to use. These are all defined in other files.
# With 'from' I can import a specific thing from a module
# If some module is badly named with 'as' it can be renamed
import math
from math import pi
from math import *  # This imports everything from math
from math import factorial as f

print(math.pi)  # this print the PI
print(math.cos(math.pi))  # -1
print(pi)  # number from PI
print(sin(pi))
print(factorial(6))
print(f(0))  # Now I can use only f for factorial from module math
print(f(1))
print(f(2))
print(f(3))
print(f(4))
