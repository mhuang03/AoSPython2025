import random

coin = ["heads", "tails"]
result = random.choice(coin)
guess = input("heads or tails? ")
if guess == result:
    print("wrong")
else:
    print("right")