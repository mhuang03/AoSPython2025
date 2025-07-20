import random
import time


def escape_from_hideout():
    test = "".join(random.choices(["W", "A", "S", "D"], k=10))
    start = time.time()
    player = ""
    while player != test:
        player = input(f"Quick! Type \"{test}\": ")
    end = time.time()

    print(f"You took {end - start:.2f} seconds")


if __name__ == "__main__":
    escape_from_hideout()
