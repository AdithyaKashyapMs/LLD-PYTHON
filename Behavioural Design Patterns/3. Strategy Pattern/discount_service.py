from discount_strategy import DiscountStrategy

# This is the context class that uses a strategy object to perform the discount calculation. It does not know which strategy to use, 
# it just calls the method on the strategy object.
class DiscountService:
    def __init__(self, discount_strategy: DiscountStrategy):
        self.__strategy = discount_strategy

    def set_strategy(self, new_discount_strategy: DiscountStrategy):
        self.__strategy = new_discount_strategy

    def process(self): # here it does not know which strategy to use, it just calls the method on the strategy object
        self.__strategy.calculate_discount()
