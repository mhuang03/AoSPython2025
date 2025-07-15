num = 1

perfect_count = 0
while perfect_count < 4:
    factor_sum = 0

    for i in range(1, num):
        if num % i == 0:
            factor_sum += i

    if factor_sum == num:
        print(num)
        perfect_count += 1

    num += 1
