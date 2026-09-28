from location import Location
from vehicle import Vehicle
from driver import Driver
from ride_sharing_service import RideSharingServiceApp
from passenger import Passenger

loc1 = Location(12.9716, 77.5946)  # Bangalore
loc2 = Location(12.2958, 76.6394)  # Mysore
loc3 = Location(13.0827, 80.2707)  #

car = Vehicle("Toyota", "Car")
bike = Vehicle("Yamaha", "Bike")

driver1 = Driver("Adithya", loc2, car)
driver2 = Driver("Ramesh", loc3, bike)

passenger1 = Passenger("John", loc1)
passenger2 = Passenger("abhi", loc2)

ride_sharing_service = RideSharingServiceApp()
ride_sharing_service.add_driver(driver1)
ride_sharing_service.add_driver(driver2)
ride_sharing_service.add_passenger(passenger1)
ride_sharing_service.add_passenger(passenger2)

ride_sharing_service.bookRide(passenger1, 19)
ride_sharing_service.bookRide(passenger2, 50)