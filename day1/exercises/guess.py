import random
ans = random.randint(1, 100)

guess = int(input("Guess a number: "))
while guess != ans:
    if guess > ans:
        print("too high!")
    elif guess < ans:
        print("too low!")
    guess = int(input("Guess a number: "))
print("You got it!")