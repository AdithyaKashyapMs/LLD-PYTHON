from abc import ABC, abstractmethod
from vehicle import Vehicle

class FareStrategy(ABC):
    @abstractmethod
    def calFare(self, vehicle: Vehicle, distance: float) -> float:
        pass

# This strategy will be decided on runtime based on the type of ride (Standard, Shared, Luxury, etc.)
class StandardFareStrategy(FareStrategy):
    def calFare(self, vehicle, distance):
        return vehicle.get_fare_amount() * distance

class SharedFareStrategy(FareStrategy):
    def calFare(self, vehicle, distance):
        return (vehicle.get_fare_amount() * distance) * 0.5  # Assuming a 20% discount for shared rides

class LuxuryFareStrategy(FareStrategy):
    def calFare(self, vehicle, distance):
        return (vehicle.get_fare_amount() * distance) * 1.5