# print(__name__)

def first_half(s):
    return s[:len(s) / 2]


def last_half(s):
    return s[len(s) / 2:]


# We are currently running THIS script
if __name__ == '__name__':
    print("Testing string functions")
    assert first_half("abcd") == "ab", "First half is failing"
    assert last_half("abcd") == "cd", "Last half is failing"
