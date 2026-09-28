from location import Location
from vehicle import Vehicle

class Driver:
    def __init__(self, name, location: Location, vehicle: Vehicle, ):
        self.name = name 
        self.location: Location = location
        self.vehicle:Vehicle = vehicle
        # Can have more attributes like status assigned or free

    def get_location(self) -> Location:
        return self.location

    def set_location(self, location: Location) -> None:
        self.location = location 

