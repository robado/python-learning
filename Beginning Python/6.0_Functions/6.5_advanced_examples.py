#! /usr/bin/python
# 6.5 Advanced Examples

# Shift cipher

alpha = "abcdefghijklmnopqrstuvwxyz"  # lenght 26


# So this function takes the string and loops the string, find characters, where is the character, find the index,
# do the shift, then crab the character and put it into a variable .
def encrypt(s, shift=3):
    encrypted_str = ""
    for c in s:
        index = alpha.index(c)
        shifted_index = (index + shift) % len(alpha) # This is for rap around to happen
        encrypted_str += alpha[shifted_index]
    return encrypted_str


def decrypt(e, shift=3):
    decrypted_str = ""
    for c in e:
        index = alpha.index(c)
        shifted_index = (index - shift) % len(alpha)
        decrypted_str += alpha[shifted_index]
    return decrypted_str


print(encrypt("helloworld"))
print(decrypt("khoorzruog"))
print(decrypt(encrypt("heihello")))
