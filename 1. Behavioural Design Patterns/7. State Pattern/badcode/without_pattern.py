from enum import Enum

class TransportMode(Enum):
    WALKING = "waliking"
    BIKE = "Bike"
    TRAIN = "Train"

class TransportService:
    def __init__(self, transport_mode: TransportMode):
        self.__transport_mode: TransportMode = transport_mode

    def set_mode(self, transport_mode: TransportMode):
        self.__transport_mode = transport_mode

    """ Here it is messy and not scalabel if we have new methods of transport we have to 
    # add new if else statements to the methods below, this is not a good design
    # we can use state pattern to solve this problem and make the code more scalabe and pre
    # serve the open closed principle, so that we can add new transport modes without changing the existing code"""
    def eta(self):
        if self.__transport_mode == TransportMode.WALKING:
            print("Walking will take 15 minutes")
        elif self.__transport_mode == TransportMode.BIKE:
            print("Bike will take 10 minutes")
        elif self.__transport_mode == TransportMode.TRAIN:
            print("Train will take 5 minutes")

    def directions(self):
        if self.__transport_mode == TransportMode.WALKING:
            print("Go straight and take left")
        elif self.__transport_mode == TransportMode.BIKE:
            print("Go to flyoverand take right")
        elif self.__transport_mode == TransportMode.TRAIN:
            print("Train train to station and take left")
