# Problem 3: Factorial
# Write a program that asks the user for a number n and then calculates the factorial of that number.
# The factorial of a number n is the product of all positive integers less than or equal to n.
# For example, the factorial of 5 is 5 * 4 * 3 * 2 * 1 = 120.
# Hint: Use a loop to multiply the numbers from 1 to n together.

n = int(input("Enter a number: "))

product = 1

while n > 1:
    product = n * product
    n = n - 1

print(product)