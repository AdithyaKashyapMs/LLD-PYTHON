
from abc import ABC, abstractmethod


class Beverage(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> int:
        pass

class Coffee(Beverage):
    def get_description(self) -> str:
        return "Simple Plane Coffee"

    def get_cost(self) -> int:
        return 20

class CoffeeWithMilk(Coffee):
    def get_description(self) -> str:
        return "Plane Coffee with Milk"

    def get_cost(self) -> int:
        return 25

# Now like how much can we do with 10 paramters 2**10 combinations of coffee with different ingredients.

coffee1 = CoffeeWithMilk()
print(coffee1.get_description())
print(coffee1.get_cost())

# This is not good example
# Lots of lots of code classes 
