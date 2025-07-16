start = [3, 10, 17, 24, 31, 38]
diffs = [start]

for _ in range(len(start) - 1):
    next_diff = []
    last = diffs[-1]
    for i in range(len(last) - 1):
        next_diff.append(last[i+1] - last[i])
    diffs.append(next_diff)

for diff in diffs:
    print(diff)
