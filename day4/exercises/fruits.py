class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"{self.color} {self.name}"

    def __repr__(self):
        return f"{self.color} {self.name}"


fruits = [
    Fruit("apple", "red"), Fruit("strawberry", "red"),
    Fruit("raspberry", "red"), Fruit("orange", "orange"),
    Fruit("mango", "yellow"), Fruit("banana", "yellow"),
    Fruit("grape", "purple"), Fruit("cherry", "red"),
    Fruit("pear", "green"), Fruit("pomegranate", "red"),
    Fruit("cranberry", "red")
]
print(fruits)


color_dict = {}
for fruit in fruits:
    if fruit.color not in color_dict:
        color_dict[fruit.color] = [fruit]
    else:
        color_dict[fruit.color].append(fruit)

print(color_dict)