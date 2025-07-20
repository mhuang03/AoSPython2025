def fibonacci(n: int):
    if n <= 1:
        print(n)
        return

    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a+b

    print(b)


for i in range(10):
    fibonacci(i)