class Bike:
       def __init__(self, colour, material, brand):
              self.colour= colour
              self.material = material
              self.brand = brand


       def brake(self):
              print("Braking")


red_bike = Bike('Red', 'Steel', 'Honda')

print(red_bike.colour)
print(red_bike.material)
print(red_bike.brand)
red_bike.brake()

