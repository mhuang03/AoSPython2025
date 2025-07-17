class Vehicle:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def __str__(self):
        return f"{self.year} {self.make} {self.model} with {self.mileage} miles"

    def drive(self, miles):
        self.mileage += miles


car1 = Vehicle("Honda", "Accord", 2007, 100000)
car2 = Vehicle("Hyundai", "Elantra", 2016, 40000)
print(car1)
print(car1.make)
print(car1.model)
print(car1.year)
print(car1.mileage)
car1.drive(100)
print(car1.mileage)

print()
print(car2.make)
print(car2.model)
print(car2.year)
print(car2.mileage)
car2.drive(200)
print(car2.mileage)

