class Chef:
    def cook_pasta(self):
        print("Chef is cooking pasta")

    def cook_pizza(self):
        print("Chef is cooking pizza")

    # when we add a new dish, we need to modify the Chef class, 
    # which violates the Open/Closed Principle.
    # we need to change the waiter class to add a new dish, which violates the Open/Closed Principle.
    def cook_burger(self):
        print("Chef is cooking burger")

class Waiter:
    def __init__(self, chef: Chef):
        self.__chef = chef

    def place_order(self, order: str):
        if order == "pasta":
            self.__chef.cook_pasta()
        elif order == "pizza":
            self.__chef.cook_pizza()
        # when we add a new dish, we need to modify the Waiter class,
        # such as burger, which violates the Open/Closed Principle.
        elif order == "burger":
            self.__chef.cook_burger()
        else:
            print("Sorry, we don't serve that dish.")

chef = Chef()
waiter = Waiter(chef)
waiter.place_order("pasta")
waiter.place_order("pizza")
waiter.place_order("burger")