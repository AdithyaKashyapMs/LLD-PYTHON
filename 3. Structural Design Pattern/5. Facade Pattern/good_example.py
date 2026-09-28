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

class ApiGateway:
    def __init__(self):
        self.__user_service = UserService()
        self.__order_service = OrderService()

    def login_user(self, username: str, password: str) -> dict:
        return self.__user_service.login(username, password)

    def get_user_profile(self, user_id: str) -> dict:
        return self.__user_service.get_profile(user_id)

    def get_order_details(self, user_id: str) -> list:
        return self.__order_service.get_orders(user_id)

    # now what if i make a new method
    def get_all_details(self, user_id, username, password):
        user_info = self.__user_service.login(username, password)
        profile_info = self.__user_service.get_profile(user_id)
        order_info = self.__order_service.get_orders(user_id)
        return {
            "user_info": user_info,
            "profile_info": profile_info,
            "order_info": order_info
        }


api_gateway = ApiGateway()
all_details = api_gateway.get_all_details("U!23", "root", "pass")
print("\nAll details retrieved:")
print(all_details)
# so if the userService changes its method to loginn_user instead of login, we will have to change the client code as well. 
# This helps in decoupling the client code from the implementation of the services. # but then we need to change APIGateway class as well 
# which violates the open/closed principle.