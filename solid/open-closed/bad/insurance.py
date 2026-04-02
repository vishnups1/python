import datetime

from vehicle import Vehicle
from car import Car
from truck import Truck

"""
Insurance class is not closed for modification because it needs to be modified if a new vehicle type is added.

If a new vehicle type is added, the Insurance class needs to be modified to calculate the insurance for the new vehicle type.
"""

class Insurance:
    def __init__(self, vehicle: Vehicle):
        self.vehicle = vehicle

    def calculate_insurance(self):
        age = datetime.now().year - self.vehicle.year
        if isinstance(self.vehicle, Car):
            if age < 5:
                return 1000
            else:
                return 1500
        elif isinstance(self.vehicle, Truck):
            if age < 5:
                return 1500
            else:
                return 2000
        else:
            raise ValueError("Invalid vehicle type")
