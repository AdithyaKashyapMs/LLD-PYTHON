from order import Order
from chef import Chef

class BurgerOrder(Order):
    def __init__(self, chef: Chef):
        self.__chef = chef

    def execute(self):
        print("Order received: Burger")
        self.__chef.cook_burger()
