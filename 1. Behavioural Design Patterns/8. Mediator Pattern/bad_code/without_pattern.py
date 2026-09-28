"""
    A class to represent an airplane.
    This class has a flight number and can send messages to other airplanes.
    Here spice jet needs to send  messages to other airplanes, 
    but it needs to know the details of how the messages are sent,"""
# This makes very messy and not scalable, code 

# This can be solved using mediator pattern, where we can have a mediator class which will handle the communication between the airplanes and spice jet will not know the details of how the messages are sent, it will just call the send_message method on the mediator class and the mediator class will handle the communication between the airplanes.
class Airplane:
    def __init__(self, flight_number):
        self.__flight_number = flight_number

    def send_message(self, msg: str, airplane: "Airplane"):
        print(f"{self.__flight_number} is sending {msg} to {airplane.get_flight_number()} ")

    def get_flight_number(self):
        return self.__flight_number

spicejet = Airplane("SpiceJet 123")
indigo = Airplane("Indigo 1113")
air_inida = Airplane("Air India 12121")

spicejet.send_message("Landing on runway", indigo)
spicejet.send_message("Landing on runway", air_inida)
