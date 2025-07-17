import random


def roll_dice(n, s):
    total = 0

    for _ in range(n):
        total += random.randint(1, s)

    return total


for _ in range(10):
    print(roll_dice(100000, 120))
