n = int(input("Enter a number (at least 2): "))

fibs = [0, 1]
for _ in range(2, n):
    fibs.append(fibs[-1] + fibs[-2])

print(fibs)

approx = []
for i in range(1, len(fibs) - 1):
    approx.append(fibs[i+1]/fibs[i])

print(approx)