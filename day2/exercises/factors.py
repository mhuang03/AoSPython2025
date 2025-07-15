num = int(input("Enter a number: "))

factor_count = 0
for i in range(1, num+1):
    if num % i == 0:
        factor_count += 1
        print(i)

if factor_count == 2:
    print("Number is prime!")