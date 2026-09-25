from abc import ABC, abstractmethod

# This is a good example of the Abstract Factory Pattern. The RestaurantService class is not tightly coupled with the concrete classes PaneerTikka, ButterChicken, GulabJamun, MeduVada, Dosa, and Payasam. If we want to add a new cuisine type, we don't have to modify this class. This is in accordance with the Open/Closed Principle.

# This Starter is a base class for all the starters. 
# the concrete classes PaneerTikka and MeduVada are derived from this base class.
class Starter(ABC):
    @abstractmethod
    def prepare(self):
        pass
 
# This MainCourse is a base class for all the main courses.
# the concrete classes ButterChicken and Dosa are derived from this base class.
class MainCourse(ABC):
    @abstractmethod
    def prepare(self):
        pass

# This Dessert is a base class for all the desserts.
# the concrete classes GulabJamun and Payasam are derived from this base class.
class Dessert(ABC):
    @abstractmethod
    def prepare(self):
        pass

class PaneerTikka(Starter):
    def prepare(self):
        print("Preparing Paneer Tikka(North Indian Starter)")

class ButterChicken(MainCourse):
    def prepare(self):
        print("Preparing Butter Chicken(North Indian Main Course)")

class GulabJamun(Dessert):
    def prepare(self):
        print("Preparing Gulab Jamun(North Indian Dessert)")


class MeduVada(Starter):
    def prepare(self):
        print("Preparing Medu Vada(South Indian Starter)")

class Dosa(MainCourse):
    def prepare(self):
        print("Preparing Dosa(South Indian Main Course)")

class Payasam(Dessert):
    def prepare(self):
        print("Preparing Payasam(South Indian Dessert)")

# This CuisineFactory is an abstract factory class that defines the methods for creating the different types of food items.
#  The concrete classes NorthIndianCuisine and SouthIndianCuisine implement these methods to create the specific food items for each cuisine type.
class CuisineFactory(ABC):
    @abstractmethod
    def create_starter(self) -> Starter:
        pass

    @abstractmethod
    def create_main_course(self) -> MainCourse:
        pass

    @abstractmethod
    def create_dessert(self) -> Dessert:
        pass

# The NorthIndianCuisine is a concrete factory class that implements the methods of the CuisineFactory class to create the specific food items for the North Indian cuisine type.
class NorthIndianCuisine(CuisineFactory):
    def create_starter(self) -> Starter:
        return PaneerTikka()

    def create_main_course(self) -> MainCourse:
        return ButterChicken()

    def create_dessert(self) -> Dessert:
        return GulabJamun()

# The SouthIndianCuisine is a concrete factory class that implements the methods of the CuisineFactory class to create the specific food items for the South Indian cuisine type.
class SouthIndianCuisine(CuisineFactory):
    def create_starter(self) -> Starter:
        return MeduVada()

    def create_main_course(self) -> MainCourse:
        return Dosa()

    def create_dessert(self) -> Dessert:
        return Payasam()

# The RestaurantService class is a client class that uses the CuisineFactory to create the different types of food items.
#  It is not tightly coupled with the concrete classes PaneerTikka, ButterChicken, GulabJamun, MeduVada, Dosa, and Payasam. If we want to add a new cuisine type, we don't have to modify this class. This is in accordance with the Open/Closed Principle.
# This presents a good example of the Abstract Factory Pattern. The RestaurantService class is not tightly coupled with the concrete classes PaneerTikka, ButterChicken, GulabJamun, MeduVada, Dosa, and Payasam. If we want to add a new cuisine type, we don't have to modify this class. 
# This is in accordance with the Open/Closed Principle.
class RestaurantService:
    def __init__(self, factory: CuisineFactory):
        self.__factory = factory

    def create_meal(self):
        starter = self.__factory.create_starter()
        main_course = self.__factory.create_main_course()
        dessert = self.__factory.create_dessert()

        starter.prepare()
        main_course.prepare()
        dessert.prepare()

    def change_cuisine(self, new_factory: CuisineFactory):
        self.__factory = new_factory
north_indian_cuisine = NorthIndianCuisine()
restaurant_service = RestaurantService(north_indian_cuisine)
restaurant_service.create_meal()

south_indian_cuisine = SouthIndianCuisine()
restaurant_service.change_cuisine(south_indian_cuisine)
restaurant_service.create_meal()
# Now, if we want to change the cuisine type to Chinese 
# we can create a new concrete factory class ChinsesCuisine that 
# implements the methods of the CuisineFactory class to create the specific food items for the Chinese cuisine type.

# The Flow of code is as follows:
# 1. The client (RestaurantService) creates an instance of the concrete factory (NorthIndianCuisine) and passes it to the RestaurantService constructor.
# 2. The RestaurantService class uses the factory to create the different types of food items
# 3. The client can change the cuisine type by creating a new instance of the concrete factory (SouthIndianCuisine) and passing it to the change_cuisine method of the RestaurantService class.
# 4. The RestaurantService class uses the new factory to create the different types of food items.
# 5. The client can change the cuisine type to any other cuisine type by creating a new instance of the concrete factory and passing it to the change_cuisine method of the RestaurantService class.
