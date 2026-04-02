import datetime

from vehicle import Vehicle

"""
Insurance class is closed for modification because it does not need to be modified if a new vehicle type is added.

If a new vehicle type is added, the Insurance class does not need to be modified to calculate the insurance for the new vehicle type.
"""

class Insurance:
    def calculate_insurance(self, vehicle: Vehicle):
        return vehicle.calculate_insurance()
