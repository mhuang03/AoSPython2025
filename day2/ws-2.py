# Problem 2: Triangle
# Write a program that asks the user for a number n and then prints a triangle with n rows.
# For example, if the user enters 5, the program should print:
# *
# **
# ***
# ****
# *****
# Hint: Use nested loops to print the rows of the triangle. Use print(text, end='') to print on the same line.

num = int(input("Enter a number: "))

for i in range(num):  # num rows
    for _ in range(i + 1):  # individual row, on row i we want i+1 asterisks
        print("* ", end='')
    print()
