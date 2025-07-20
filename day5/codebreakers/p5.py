import time


def deep_breaths(n: int):
    for _ in range(n):
        print("breathe in")
        time.sleep(5)
        print("breathe out")
        time.sleep(5)


deep_breaths(2)