from location import Location
from abc import ABC, abstractmethod

class User(ABC):
    def __init__(
            self, 
            name: str, 
            email: str,
            location: Location
    ):
        self.name: str = name
        self.email: str = email
        self.location: Location = location

    def get_name(self) -> str:
        return self.name

    def get_location(self) -> Location:
        return self.location

    def set_location(self, new_location: Location):
        self.location = new_location

    @abstractmethod
    def notify(self):
        pass