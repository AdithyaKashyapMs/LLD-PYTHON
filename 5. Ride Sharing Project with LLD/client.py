from location import Location
from car import Car
from bike import Bike
from driver import Driver
from ride_matching_service import RideMatchingService
from passenger import Passenger
from fare_strategy import  LuxuryFareStrategy

loc1 = Location(12.9716, 77.5946)  # Bangalore
loc2 = Location(12.2958, 76.6394)  # Mysore
loc3 = Location(13.0827, 80.2707)  #

car = Car("KA3-AB-1234")
bike = Bike("KA-01-AB-1234")

driver1 = Driver("Adithya", "abc@example.com", loc2, car)

passenger1 = Passenger("John", "john@example.com", loc2)


ride_matching_service = RideMatchingService()
ride_matching_service.add_driver(driver1)
ride_matching_service.requestRide(passenger1, 50, LuxuryFareStrategy())