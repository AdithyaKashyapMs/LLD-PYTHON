from user import User
from vehicle import Vehicle

class Driver(User):
    def __init__(self, name, email, location, vehicle: Vehicle):
        super().__init__(name, email, location)
        self.__vehicle = vehicle

    def get_vehicle(self) -> Vehicle:
        return self.__vehicle


    def notify(self, msg: str):
        print(f"Notification for Driver {self.get_name()}: {msg}")
