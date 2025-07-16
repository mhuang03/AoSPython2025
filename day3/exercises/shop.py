prices = {"apple": 2.50, "orange": 3, "banana": 1}
total = 0

while True:
    response = input("What do you want: ")

    if response == "done":
        break
    elif response in prices:
        total += prices[response]
    else:
        print("We don't have that")

print(f"Your total is: ${total:.2f}")
