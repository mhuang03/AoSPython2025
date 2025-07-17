class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)

    def print(self):
        for _ in range(self.b):
            print("* " * self.a)


r1 = Rectangle(3, 5)
print(r1.area())
print(r1.perimeter())
r1.print()

r2 = Rectangle(18, 22)
print(r2.area())
print(r2.perimeter())
r2.print()