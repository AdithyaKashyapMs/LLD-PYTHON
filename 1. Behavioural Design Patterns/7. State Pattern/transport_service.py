from transport_mode import TransportMode

class TransportService:
    def __init__(self, mode: TransportMode):
        self.__mode = mode

    def set_mode(self, new_mode: TransportMode):
        self.__mode = new_mode

    def eta(self):
        self.__mode.eta()

    def directions(self):
        self.__mode.directions()
    