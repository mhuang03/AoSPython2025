text = input("Type something: ")

vowel_count = 0
for c in text:
    if c in "aeiouAEIOU":
        vowel_count += 1
print(f"You typed {vowel_count} vowels.")