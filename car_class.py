class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"The {self.brand} {self.model} is now driving.")

brand = input("Enter car brand: ")
model = input("Enter car model: ")

my_car = Car(brand, model)

my_car.drive()
