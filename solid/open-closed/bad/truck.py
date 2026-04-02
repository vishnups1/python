from vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year)
        self.color = color

    def get_info(self):
        return f"{super().get_info()} {self.color}"
