message = input("Type something: ")
chars = set()

for char in message:
    chars.add(char)

print(f"You typed {len(chars)} unique character{'s' if len(chars) != 1 else ''}")

# ternary expression
# a = "a"
# b = "b"
# condition = True
# print(a if condition else b)
