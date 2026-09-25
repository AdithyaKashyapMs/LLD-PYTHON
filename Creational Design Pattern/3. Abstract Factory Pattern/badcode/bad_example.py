from abc import ABC, abstractmethod

# This is a bad example of the Abstract Factory Pattern. The RestaurantService class is tightly coupled 
# with the concrete classes PaneerTikka, ButterChicken, GulabJamun, MeduVada, Dosa, and Payasam. If we
#  want to add a new cuisine type, we have to modify this class. This is a violation of the Open/Closed Principle.
class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass

class PaneerTikka:
    def prepare(self):
        print("Preparing Paneer Tikka(North Indian Starter)")

class ButterChicken:
    def prepare(self):
        print("Preparing Butter Chicken(North Indian Main Course)")

class GulabJamun:
    def prepare(self):
        print("Preparing Gulab Jamun(North Indian Dessert)")


class MeduVada:
    def prepare(self):
        print("Preparing Medu Vada(South Indian Starter)")

class Dosa:
    def prepare(self):
        print("Preparing Dosa(South Indian Main Course)")

class Payasam:
    def prepare(self):
        print("Preparing Payasam(South Indian Dessert)")

class RestaurantService:
    def create_order(self, cuisine_type: str):
        if cuisine_type == "north":
            starter = PaneerTikka()
            main_course = ButterChicken()
            dessert = GulabJamun()
        elif cuisine_type == "south":
            starter = MeduVada()
            main_course = Dosa()
            dessert = Payasam()
        # if we want to add a new cuisine type, we have to modify this class.
        #  This is a violation of the Open/Closed Principle.
        else:
            print("Invalid cuisine type")
            return None

        starter.prepare()
        main_course.prepare()
        dessert.prepare()

restaurant_service = RestaurantService()
restaurant_service.create_order("north")
        