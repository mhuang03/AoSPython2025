# Problem 2: Quadratic Formula
# Ask the user for the coefficients a,b,c of a quadratic in ax^2+bx+c=0 form.
# Then, compute the real roots of the equation and print them out.
# If you don't know the quadratic formula, either Google it or skip this one for now.
# Hint: use the discriminant to determine whether solutions are real.
import math
math.sqrt(9)  # == 3, square root function

a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))

discriminant = b**2 - 4*a*c

if discriminant < 0:
    print("No real solutions")
elif discriminant == 0:
    print(-b/(2*a))
else:
    print(
        (-b + math.sqrt(discriminant)) / (2*a),
        (-b - math.sqrt(discriminant)) / (2*a)
    )