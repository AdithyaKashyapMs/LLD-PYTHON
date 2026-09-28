from math import sqrt

class Location:
    def __init__(self, lat: float, long: float):
        self.__lat = lat
        self.__long = long

    def get_latitude(self):
        return self.__lat

    def get_longitude(self):
        return self.__long

    def calcDistance(self, loc: "Location"):
            # Euclidean Distance formula to calculate distance
            dx:float = self.get_latitude() - loc.get_latitude()
            dy:float = self.get_longitude() - loc.get_longitude()
            return sqrt(dx * dx + dy * dy)
