words = set()

for i in range(5):
    word = input(f"Enter a word ({i} of 5): ")
    if word in words:
        print("That was a repeat.")
    words.add(word)

# if len(words) != 5:
#     print("You typed a repeat")