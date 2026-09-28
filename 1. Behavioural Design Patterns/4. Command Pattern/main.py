from chef import Chef 
from burger_order import BurgerOrder
from pizza_order import PizzaOrder
from waiter import Waiter

# first we create the chef object which will be used to create the order objects
chef = Chef()
# then we create the order objects for burger and pizza
burger_order = BurgerOrder(chef)
pizza_order = PizzaOrder(chef)

# Now the waiter takes the order and executes it
# He does not know the details of how the order is executed, he just calls the execute method on the order object

waiter = Waiter()
waiter.take_order(burger_order)

# the OUTPUT will be:
# Order received: Burger
# Chef is cooking burger