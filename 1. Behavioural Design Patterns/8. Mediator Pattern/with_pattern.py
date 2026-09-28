from abc import ABC, abstractmethod
from typing import List

"""Here we define the mediator pattern,
    where the control tower acts as a mediator between the airplanes 
    and the airplanes do not need to know the details of how the message are sent,
    they just call the send_message method on the control tower and the control tower 
    will handle the communicatin between the airplanes and sedn the message to 
    the other airplanes"""
""" Here is the AirTrafficControl interface which will be implemented by the ControlTower class
    and it will have the methods to register the airplanes and send messages between the airplanes"""

class AirTrafficControl(ABC):
    @abstractmethod
    def register_airplane(self, new_airplane: "Airplane"):
        pass

    @abstractmethod
    def send_message(self, msg: str, sender: "Airplane"):
        pass

"""We have the ControlTower class which implements the AirTrafficControl interface and
    it will handle the communication between the airplanes and send the messages to the other airplanes
    (The init method will have a list of airplanes which are registered with the control tower and
    the send_message method will send the message to all the airplanes except the sender airplane
    The register_airplane method will add the new airplane to the list of airplanes registered with the control tower)"""
class ControlTower(AirTrafficControl):
    def __init__(self):
        self.__airplanes: List[Airplane] = []

    def register_airplane(self, new_airplane: "Airplane"):
        self.__airplanes.append(new_airplane)

    def send_message(self, msg: str, sender: "Airplane"): # Renamed parameter to sender
        for airplane in self.__airplanes:
            if airplane != sender: # Corrected comparison
                airplane.recieve_message(msg, sender)



"""The Airplane class represents an airplane in the air traffic control system.
    It has a flight number and a reference to the control tower.
    The send_message method sends a message to the control tower, which then forwards it to all other registered airplanes.
    The recieve_message method is called by the control tower to deliver messages from other airplanes.
    The get_flight_number method returns the flight number of the airplane.
    The constructor of the Airplane class takes a flight number and a reference to the control tower.
    It registers the airplane with the control tower upon creation.
    The send_message method takes a message as input and sends it to the control tower.
    The recieve_message method takes a message and the sender airplane as input and prints the received message"""
class Airplane:
    def __init__(self, flight_number, tower: "ControlTower"):
        self.__flight_number = flight_number
        self.__tower = tower # asssign the control tower to the airplane

        self.__tower.register_airplane(self) # register the airplane with the control tower

    def send_message(self, msg: str): # send message to the control tower
        self.__tower.send_message(msg, self)

    def get_flight_number(self) -> str: # return the flight number of the airplane 
        return self.__flight_number

    # takes in the message and the sender airplane and prints the recieved message 
    # This method is called by the control tower to deliver messages from other airplanes 
    # Notice that the airplane does not know the details of how the message is sent,
    #  it just receives the message from the control tower

    # This is the key point of the mediator pattern, where the airplanes do not need to know the details of how the messages are sent, 
    # they just call the send_message method on the control tower and the control tower will handle the communication between the airplanes
    # and send the message to the other airplanes
    def recieve_message(self, msg: str, who_sent: "Airplane"): 
        print(f"{self.__flight_number} got {msg} from {who_sent.get_flight_number()}")


# first we create the control tower and then we create the airplanes and register them with the control tower
control_tower = ControlTower()

# Next we create the airplanes and register them with the control tower
spicejet = Airplane("SpiceJet 123", control_tower)
indigo = Airplane("Indigo 1113", control_tower)
air_india = Airplane("Air India 12121", control_tower)

# Now we can send messages between the airplanes using the control tower as a mediator
spicejet.send_message("Landing on runway")

express = Airplane("Express 123", control_tower)
express.send_message("Only I will land on runway, you all wait for me")