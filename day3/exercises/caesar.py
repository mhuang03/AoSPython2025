message = input("Enter your message: ")
shift = int(input("Shift: "))

alphabet = "abcdefghijklmnopqrstuvwxyz"
caesar = {}
for i in range(26):
    caesar[alphabet[i]] = alphabet[(i + shift) % 26]

message = message.lower()
encoded = ""
for char in message:
    if char in caesar:
        encoded += caesar[char]
    else:
        encoded += char

print(encoded)
