from typing import List
from driver import Driver
from passenger import Passenger
from location import Location
from fare_strategy import FareStrategy
from ride import Ride, RideStatus


class RideMatchingService:
    def __init__(self):
        self.drivers: List[Driver] = []
        self.__available_drivers: List[Driver] = []

    def add_driver(self, driver: Driver):
        self.__available_drivers.append(driver)

    def requestRide(self, passenger: Passenger, distance: float, strategy: FareStrategy):
        if len(self.__available_drivers) == 0:
            passenger.notify("No drivers available")
            return 

        # Nearest Driver
        nearestDriver: Driver = self.__findNearestDriver(passenger.get_location())
        self.__available_drivers.remove(nearestDriver)
        ride: Ride = Ride(passenger, nearestDriver, distance, strategy)
        ride.calculateFare()

        passenger.notify(f"Ride has been scheduled with fare Rs. {ride.getRideFare()}")
        nearestDriver.notify(f"You have one new ride for Rs. {ride.getRideFare()}")

        ride.updateStatus(RideStatus.ONGOING)

        # AFter Sometime
        ride.updateStatus(RideStatus.COMPLETED)
        self.__available_drivers.append(nearestDriver)
        return 

    def __findNearestDriver(self, passenger_location: Location) -> Driver:
        assignedDriver = None
        minDistance = float("inf")
        for driver in self.__available_drivers:
            dist = driver.get_location().calcDistance(passenger_location)
            if dist < minDistance:
                minDistance = dist
                assignedDriver = driver
        return assignedDriver


