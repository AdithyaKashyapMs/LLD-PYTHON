
from order import Order


# Here is the Waiter class that takes orders and executes them
# It does not know the details of how the orders are executed, 
# it just calls the execute method on the order object
# and takes the specific order 
class Waiter:
    def take_order(self, order: Order):
        order.execute()
