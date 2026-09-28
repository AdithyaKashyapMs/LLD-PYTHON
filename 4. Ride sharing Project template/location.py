class Location:
    def __init__(self, lat: float, long: float):
        self.__lat = lat
        self.__long = long

    def get_latitude(self):
        return self.__lat

    def get_longitude(self):
        return self.__long