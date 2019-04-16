#! /usr/bin/python
# 6.4 Working with Examples

# => "123" -> "321"
# => "abcd" -> "dcba"
# => "11121" -> "12111"
# This function goes through the string and then ands every char into variable in reverse
def revese(s):
    # If not wrtiting pass it the function would give an error
    # pass  # code placeholder
    new_str = ""
    for i in range(len(s)):
        new_str += s[len(s) - i - 1]
    return new_str


print(revese("123"))
print(revese("abcd"))
print(revese("11121"))


# is_palindrome
# palindrome examples: "1", "121", "abba", "56765", "bbbbb", "",
# This function test that the string is palindrome or not
# Void function can have a "return" statement. But in here it stops the function and exits
def is_palindrome(p):
    # pass
    # Have to check only half of the string
    for i in range(len(p) // 2):
        if p[i] != p[len(p) - i - 1]:
            print("Yes this is not palindrome")
            return  # exit function
    # is palindrome
    print("Yes this is a palindrome")


print(is_palindrome("1"))
print(is_palindrome("121"))
print(is_palindrome("abba"))
print(is_palindrome("56765"))
print(is_palindrome("bbbb"))
print(is_palindrome(""))
print(is_palindrome("Hello"))
# Because "return" return "None" or "Yes", printing is redundant
print("")
is_palindrome("Hello")
is_palindrome("11111")
