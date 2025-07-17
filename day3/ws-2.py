# Problem 2: Isogram
# Design a function that accepts a string and returns True if the string is an isogram,
# and False otherwise. An isogram is a word or phrase without any repeating letters.
# For example, "hello" is not an isogram, but "world" is.
# Hint: Use a set to store the letters in the string and check for duplicates.

def is_isogram(string):
    # letters = set()
    # for char in string:
    #     letters.add(char)
    letters = set(string)
    return len(string) == len(letters)


print(is_isogram("hello"))
print(is_isogram("world"))
