from abc import ABC, abstractmethod
class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass

class Pizza:
    def prepare(self):
        print("Preparing Pizza")

class Burger:
    def prepare(self):
        print("Preparing Burger")

# This class is a responsible for making objects
# This is tighly coupled with the concrete classes Pizza and Burger.
# If we want to add a new food type, we have to modify this class.
#  This is a violation of the Open/Closed Principle.
class RestaurantService:
    def create_order(self, food_type: str):
        if food_type == "pizza":
            f = Pizza()
        elif food_type == "burger":
            f = Burger()
        else:
            print("Invalid food type")
            return None
        f.prepare()
        return f

restaurant_service = RestaurantService()
restaurant_service.create_order("pizza")
