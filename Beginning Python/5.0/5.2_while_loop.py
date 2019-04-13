#! /usr/bin/python
# 5.2 While Loop

index = 0
words = ["Hello", "Worlds", "Goodbye", "Words"]

# While executes the code which is indented while the condition is TRUE
# for loop loop would look something like this
# for w in words:
#   print(name)

while index < len(words):
    # code
    word = words[index]
    print(word)
    index = index + 1

# 1 - 10
total = 0
values = 1
while values <= 10:
    total = total + values
    values = values + 1
    print(total)

# True power of while loop. Run as long until condition is met
print("Please make sure a + b = 20")
while True:
    a, b = int(input("a: ")), int(input("b: "))
    if a + b == 20:
        print("Stopping loop")
        break
    else:
        print("Please make sure a + b = 20")
