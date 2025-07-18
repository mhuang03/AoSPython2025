odd_squares = [n**2 for n in range(1, 21) if n % 2 == 1]
print(odd_squares)

strings = ["hello", "goodbye", "python", "a", "ASDFGHJKIUYTFVGHJ"]
lengths = [len(s) for s in strings]
print(lengths)

mixed = "38937fn9387ywn3ieshr"
digits = [int(char) for char in mixed if char.isdigit()]
print(digits)