from vehicle import Vehicle

class Bike(Vehicle):
    def __init__(self, number_plate):
        super().__init__(number_plate)

    def get_fare_amount(self):
        return 10  # Assuming a fixed fare amount for simplicity, can be modified based on distance or other factors