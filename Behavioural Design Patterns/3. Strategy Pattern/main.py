from discount_service import DiscountService
from diwali import DiwaliDiscount
from holi import HoliDiscount

diwali_discount = DiwaliDiscount()
holi_discount = HoliDiscount()

discount_service = DiscountService(diwali_discount)
discount_service.process()

# Change the strategy to Holi discount
discount_service.set_strategy(holi_discount)
discount_service.process()