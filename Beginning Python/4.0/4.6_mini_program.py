#! /usr/bin/python
# 4.6 Mini Program

# So in this mini program was made that it takes 2 numbers and an operator between them and spits the result out for
# example '3 * 3' will give 9. Here was also accounted that if divided by zero the program will stop! Also if the user
# won't give enough parameters the program will stop.

import sys # sys.exit() quits the program

line = input()
split = line.split()

if len(split) != 3:
    print("Wrong format")
    sys.exit()

left = int(split[0])
op = split[1]
right = int(split[2])

val = 0

if op == '+':
    val = left + right
elif op == '-':
    val = left - right
elif op == '*':
    val = left * right
elif op == '/':
    if right == 0:
        print("Division by zero. Halting")
        sys.exit()
    val = left / right
else:
    print("Uknown operator: {operator}".format(operator=op))
    sys.exit()

print('{line_expr} = {value:.2f}'.format(line_expr=line, value=val))