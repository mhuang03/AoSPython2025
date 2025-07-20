from random import randint as r


def burner_numbers(n: int):
    for _ in range(n):
        start, middle, end = r(100, 999), str(r(0, 999)), str(r(0, 9999))
        print(f"({start})-{middle.rjust(3, '0')}-{end.rjust(4, '0')}")


burner_numbers(100)