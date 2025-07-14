a = int(input("Enter side length a: "))
b = int(input("Enter side length b: "))
c = int(input("Enter side length c: "))

if a + b > c and b + c > a and a + c > b:
    print("valid triangle!")
else:
    print("your triangle sucks.")