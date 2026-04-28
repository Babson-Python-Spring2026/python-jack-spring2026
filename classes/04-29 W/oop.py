class Vehicle:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def move(self):
        return "moves"

class Boat(Vehicle):
    def move(self):
        return "sails"
    
class Car(Vehicle):
    def _init_(self, name):
        super()._init_(name)
    def move(self):
        return "drives"    

vehicles = [
    Car("Toyota"),
    Boat("Speedboat")
]

for vehicle in vehicles:
    print(f"{vehicle} {vehicle.move()}")