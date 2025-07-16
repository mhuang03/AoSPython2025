# Problem 1: No Numbers or Vowels
# Write a program that asks the user for a string and then prints the string without any numbers or vowels.
# For example, if the user enters "Hello 123 World", the program should print "Hll Wrld".
# Hint: Use a loop to iterate over the characters in the string and check if each character is a number or a vowel.

text = input("Type something: ")

new_text = ""

for char in text:
    if char not in "aeiouAEIOU1234567890":
        new_text += char

print(new_text)
