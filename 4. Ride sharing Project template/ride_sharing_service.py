from typing import List
from driver import Driver
from passenger import Passenger
from vehicle import Vehicle
from location import Location
from math import sqrt

class RideSharingServiceApp:
    # This is a high - level class but it has a calculate class which is low level class which is violating the Dependency Inversion Principle.
    #  We can create a separate class for fare calculation and distance calculation and inject it into this class. This will make the code more flexible and maintainable.
    def __init__(self):
        self.drivers: List[Driver] = []
        self.passengers: List[Passenger] = []


    # Method to add Driver
    def add_driver(self, driver: Driver):
        self.drivers.append(driver)

    # Method to add passenger
    def add_passenger(self, passenger: Passenger):
        self.passengers.append(passenger)

    def __calcDistance(self, location1: Location, location2: Location):
        # Euclidean Distance formula to calculate distance
        dx:float = location1.get_latitude() - location2.get_latitude()
        dy:float = location1.get_longitude() - location2.get_longitude()
        return sqrt(dx * dx + dy * dy)

    def __calcFare(self, vehicle: Vehicle, distance: float):
        # Fare Calculation based on vehicle type and distance
        # This is violating OCP principle if we want to add auto etc we should modify the code
        if vehicle.type == "Car":
            return distance * 20
        elif vehicle.type == "Bike":
            return distance * 12
        else:
            return distance * 8

    def bookRide(self, passenger: Passenger, distance: float):
        # Edge case
        if len(self.drivers) == 0:
            print("No drivers available for {passenger.name}")
            return 
        
        # Find the closest driver to the passenger Hard Coded
        # Find the nearest driver - o(n) time complexity (brute force)
        assignedDriver = None
        minDistance = float("inf")
        for driver in self.drivers:
            currentDriverDistance = self.__calcDistance(passenger.location, driver.location)
            if currentDriverDistance < minDistance:
                minDistance = currentDriverDistance
                assignedDriver = driver

        if not assignedDriver:
            print("No driver assigned.")
            return

        # Fare Calculated based on distance and vehicle type
        expectedFare: float = self.__calcFare(assignedDriver.vehicle, distance)

        # Check if the passenger is assigned/Alloted
        #TODO: Add a list of assigned drivers to the passenger class and add the assigned driver to that list

        #Show the driver and fare to the passenger
        print(
            f"Ride booked for {passenger.name} with driver {assignedDriver.name} with fare of Rs. {expectedFare}"
        )
        print(f" Driver is on the way and is {minDistance}km away from your location")
