from abc import ABC, abstractmethod

"""
Vehicle class is open for extension but closed for modification.

If a new vehicle type is added, the Vehicle class needs to be extended and IT SHOULD implement the get_info and calculate_insurance methods.
"""

class Vehicle(ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def get_info(self):
        return f"{self.make} {self.model} {self.year}"

    @abstractmethod
    def calculate_insurance(self):
        pass
