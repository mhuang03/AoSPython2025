n = int(input("Give me a number: "))

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3*n + 1
    print(n)