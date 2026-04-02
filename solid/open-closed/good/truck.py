from vehicle import Vehicle
from datetime import datetime

class Truck(Vehicle):
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year)
        self.color = color

    def get_info(self):
        return f"{super().get_info()} {self.color}"

    def calculate_insurance(self):
        age = datetime.now().year - self.year
        if age < 5:
            return 1500
        else:
            return 2000
