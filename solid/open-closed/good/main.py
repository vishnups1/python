from car import Car
from truck import Truck
from insurance import Insurance

car = Car("Toyota", "Corolla", 2020, "Red")
truck = Truck("Ford", "F-150", 2021, "Blue")
insurance = Insurance()

print(insurance.calculate_insurance(car))
print(insurance.calculate_insurance(truck))
