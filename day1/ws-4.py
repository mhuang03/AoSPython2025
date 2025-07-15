# Problem 4: Fibonacci
# Write a program that asks the user for a number n and then prints the first n Fibonacci numbers.
# The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones.
# The sequence starts with 0 and 1.
# For example, the first 5 Fibonacci numbers are 0, 1, 1, 2, 3.
# Hint: Use some variables to keep track of the previous 2 Fibonacci numbers.

n = int(input("Enter a number: "))
print(0)

a = 0
b = 1

while n > 1:
    print(b)
    next_fib = a + b
    a = b
    b = next_fib
    n -= 1

#   0   1   1   2   3   5
#           a   b
#                   ^next_fib