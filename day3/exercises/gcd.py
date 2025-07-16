# def gcd(a, b):
#     start = min(a, b)
#
#     for i in range(start, 0, -1):
#         if a % i == 0 and b % i == 0:
#             return i

def gcd(a, b):
    small = min(a, b)
    big = max(a, b)

    while small != 0:
        big = big - (big//small)*small
        small, big = min(small, big), max(small, big)

    return big


print(gcd(1007, 250000000000000))


# Euclidean algorithm
#   10  25
#   10  15
#   10  5
#   5   5
#   0   5
