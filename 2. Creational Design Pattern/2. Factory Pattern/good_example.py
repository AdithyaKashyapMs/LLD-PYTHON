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

class FoodFactory:
    @staticmethod
    # def create_food(self, food_type: str): as staticmethod, we don't need to pass self as the first argument. We can call this method without creating an instance of the class.
    def create_food(food_type: str):
        if food_type == "pizza":
            return Pizza()
        elif food_type == "burger":
            return Burger()
        else:
            print("Invalid food type")
            return None

class RestaurantService:
    def create_order(self, food_type: str):
        f = FoodFactory.create_food(food_type)
        if f is None:
            print("Invalid food type")
            return None
        f.prepare()
        return f

restaurant_service = RestaurantService()
restaurant_service.create_order("pizza")
