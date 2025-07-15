nums = [2, 6, 7, 14, 5, 9]

odds = []
evens = []

for n in nums:
    if n % 2 == 0:
        evens.append(n)
    else:
        odds.append(n)

print(f"odds: {odds}")
print(f"even: {evens}")


# odds = [n for n in nums if n % 2 == 1]
# print(odds)