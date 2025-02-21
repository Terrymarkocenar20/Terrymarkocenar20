class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model},Year: {self.year}")


car1 = Car("Honda", "Insight", 1999)
car2 = Car("Honda", "Pilot", 2004)

print("Car 1:")
car1.display_info()
print("Car 2:")
car2.display_info()
