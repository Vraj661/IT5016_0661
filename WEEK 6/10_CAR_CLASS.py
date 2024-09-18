class Car:
  def __init__(self, color, model, year):
    self.color = color
    self.model = model
    self.year = year

my_car = Car("black", "Tesla Model S", 2023)

print(my_car.color)
print(my_car.model)
print(my_car.year)