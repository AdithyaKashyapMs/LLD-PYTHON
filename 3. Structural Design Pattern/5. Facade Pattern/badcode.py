class UserService:
    def login(self, username: str, password: str) -> dict:
        print(f"[UserService] Logging in user: {username}")
        return {"user_id": "U!23", "name": username}
        # Logic to authenticate user
    
    def get_profile(self, user_id: str) -> dict:
        print(f"[UserService] Fetching profile for user_id: {user_id}")
        return  {"user_id": user_id, "name": "Rahul", "address": "Mumbai"}

class OrderService:
    def get_orders(self, user_id: str) -> list:
        print(f"[OrderService] Fetching orders for user_id: {user_id}")
        return [
            {"order_id": "O!23", "item": "Laptop", "price": 1000},
            {"order_id": "O!24", "item": "Mouse", "price": 50}
        ]

user_service = UserService()
order_service = OrderService()

user_service.login("root", "pass")
user_service.get_profile("U!hjkjkkjkdf")

print(order_service.get_orders("U!hjkjkkjkdf"))
# The problem with this code is that the client code is tightly coupled with the UserService and OrderService classes.
#  If we want to change the implementation of these services, we will have to change the client code as well. This violates the Open/Closed Principle.
# so we use facade pattern to provide a unified interface to a set of interfaces in a subsystem.