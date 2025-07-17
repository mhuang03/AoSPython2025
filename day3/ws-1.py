# Problem 1: Word Count
# Write a program that asks the user for some words, then prints each unique word and
# how many times it appeared.
# Hint: Use a dictionary to store the counts of each word.

counts = {}
word = input("Type a word: ")
while word != "":
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1
    word = input("Type a word: ")

for key in counts:
    print(f"You typed \"{key}\" {counts[key]} times(s).")
