# Polymorphism means many forms.

class Car:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

    def move(self):
        print("Auto Drive")


class Plane:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

    def move(self):
        print("Flying")


class Boat:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

    def move(self):
        print("Sail")


car1 = Car("Mustang", "Ford")
plane1 = Plane("747", "Boeing")
boat1 = Boat("Touring 20", "Ibiza")

for x in (car1, plane1, boat1):
    x.move()


# Inheritance Class Polymorphism
class Vehicle:
    def __init__(self, model, brand):
        self.model = model
        self.brand = brand

    def move(self):
        print("Drive")


class Car(Vehicle):
    pass


class Plane(Vehicle):
    def move(self):
        print("Flying")


class Boat(Vehicle):
    def move(self):
        print("Sail")


car2 = Car("Mustang", "Ford")
plane2 = Plane("747", "Boeing")
boat2 = Boat("Touring 20", "Ibiza")

for x in (car2, plane2, boat2):
    x.move()


