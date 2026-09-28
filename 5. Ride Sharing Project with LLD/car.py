from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, number_plate):
        super().__init__(number_plate)

    def get_fare_amount(self):
        return 20  # Assuming a fixed fare amount for simplicity, can be modified based on distance or other factors
