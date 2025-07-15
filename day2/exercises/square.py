n = int(input("Enter a side length: "))

for i in range(n):
    # print out a row of length n
    for j in range(n):
        print("*  ", end="")
    print()

# for i in range(n):
#     print("*  " * n)

# print(("*  " * n + "\n") * n)
