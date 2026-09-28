from location import Location 

class Passenger:
    def __init__(self, name: str, location: Location):
        self.name: str = name
        self.location: Location = location