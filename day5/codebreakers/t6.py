class Watch:
    def __init__(self, brand, price, superpower):
        self.brand = brand
        self.price = price
        self.superpower = superpower

    def __str__(self):
        return f"${self.price:.2f} {self.brand} watch that {self.superpower}"

    def __repr__(self):
        return str(self)


if __name__ == "__main__":
    w = Watch("BitWatch", 100, "rewinds time")
