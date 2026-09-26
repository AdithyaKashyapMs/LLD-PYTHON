
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

class AddOnDecorator(Beverage):
    def __init__(self, coffee: "Coffee"):
        self._coffee = coffee # Changed __coffee to _coffee
    def get_description(self) -> str:
        pass

    def get_cost(self) -> int:
        pass

class MilkDecorator(AddOnDecorator):
    def get_description(self):
        return self._coffee.get_description() + " with Milk" # Changed __coffee to _coffee

    def get_cost(self):
        return self._coffee.get_cost() + 5 # Changed __coffee to _coffee

class SugarDecorator(AddOnDecorator):
    def get_description(self):
        return self._coffee.get_description() + " with Sugar" # Changed __coffee to _coffee

    def get_cost(self):
        return self._coffee.get_cost() + 2 # Changed __coffee to _coffee

class ChocolateDecorator(AddOnDecorator):
    def get_description(self):
        return self._coffee.get_description() + " with Chocolate" # Changed __coffee to _coffee

    def get_cost(self):
        return self._coffee.get_cost() + 10 # Changed __coffee to _coffee

coffee = Coffee()
coffee = MilkDecorator(coffee)
coffee = ChocolateDecorator(coffee)
coffee = SugarDecorator(coffee)
print(coffee.get_description())
print(coffee.get_cost())

# WE need to only make 10 classes and not 2**10 classes for all the combinations of coffee with different ingredients. This is the power of decorator pattern. We can add new functionality to an existing object without altering its structure.