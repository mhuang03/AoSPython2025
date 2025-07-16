string = "aaabbc"
counts = {}

for char in string:
    # if char in counts:
    #     counts[char] += 1
    # else:
    #     counts[char] = 1

    if char not in counts:
        counts[char] = 0
    counts[char] += 1

print(counts)

# {
#     "a": 3,
#     "b": 2,
#     "c": 1,
# }
