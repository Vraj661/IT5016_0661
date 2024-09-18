# create a vehicle class with the methods for starting and 
# stopping, and create a car class that inherits from vehice
# and adds method for honking the horn

# output=Vehicle started
# Honk! Honk!
# Veehicle stopped

class Vehicle:
    def __init__(self,) -> None:
        pass
    def start(self):
        print("Vehicle started")

    def stop(self):
        print("Vehicle stopped")

class Car(Vehicle):
    def honk(self):
        print("Honk! Honk!")

my_car = Car()
my_car.start()
my_car.honk()
my_car.stop()
        