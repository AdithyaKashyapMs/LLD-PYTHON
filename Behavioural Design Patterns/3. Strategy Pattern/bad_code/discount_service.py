class DiscountSerivce:

    def calculate_discount(self,discount_type: str):
        if discount_type == "diwali":
            print("Applying Diwali discount")
        elif discount_type == "new_year":
            print("Applying New Year discount")
        else:
            print("No discount available")