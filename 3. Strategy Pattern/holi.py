from discount_strategy import DiscountStrategy

class HoliDiscount(DiscountStrategy):
    def calculate_discount(self):
        print("Applying Holi discount")