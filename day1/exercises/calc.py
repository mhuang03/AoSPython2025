a = int(input("Give me a number: "))
op = input("What operation? (+,-,*,/): ")
b = int(input("Give me another number: "))

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b == 0:
        print("Can't divide by 0.")
    else:
        print(a / b)
else:
    print("Operation is not valid.")