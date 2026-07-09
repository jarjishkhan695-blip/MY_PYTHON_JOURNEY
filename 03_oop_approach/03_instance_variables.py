"""
Instance Variables in Python

Instance variables belong to a specific object.
Each object can have different values.
"""

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


car1 = Car("Toyota", "Fortuner")
car2 = Car("Honda", "City")

car1.show_details()
car2.show_details()
