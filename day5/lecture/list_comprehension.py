# Syntax: [<expression> for <item> in <iterable>]
squares = [x**2 for x in range(6)]
print(squares)

# Equivalent for loop:
squares_loop = []
for x in range(6):
    squares_loop.append(x**2)
print(squares_loop)

# You can add a filter condition:
# Syntax: [<expression> for <item> in <iterable> if <condition>]
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

# Nested loops work too
# Syntax: [<expression> for <item1> in <iterable1> for <item2> in <iterable2>]
pairs = [(i, j) for i in [1, 2, 3] for j in ['a', 'b']]
print(pairs)

# equivalent for loop:
pairs_loop = []
for i in [1, 2, 3]:
    for j in ['a', 'b']:
        pairs_loop.append((i, j))
print(pairs_loop)

# You can use more complex expressions
words = ["hello", "world", "python"]
upper_words = [w.upper()[::-1] for w in words]
print(upper_words)
