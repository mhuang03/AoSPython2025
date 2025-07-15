# Problem 5: Smart Guesser
# In class, we wrote a program for a higher/lower guessing game.
# Create a program that implements a guessing strategy for the computer, where the user tells
# the program higher/lower instead. What kind of strategy can the computer use?
# Hint: If the user isn't lying, the optimal strategy for guessing 1-100 guarantees the
# correct answer in at most 7 tries.

low = 0
high = 101
guess_count = 0

while True:
    guess = (high - low) // 2 + low
    print(f"I guess {guess}")
    # print("I guess " + str(guess))
    guess_count += 1

    result = input("Was my guess too high (H), too low (L), or correct (C)? ")

    if result == "H":
        high = guess
    elif result == "L":
        low = guess
    elif result == "C":
        print(f"I won in {guess_count} guesses!")
        break
