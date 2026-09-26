from abc import ABC, abstractmethod

# Interface
class NotificationService(ABC):
    @abstractmethod
    def send(self, to: str, title: str, body: str):
        pass

class EmailNotificationService(NotificationService):
    def send(self, to: str, title: str, body: str):
        print("Sending Email through EmailNotificationService")
        print(f"To: {to}")
        print(f"Title: {title}")
        print(f"Body: {body}")

class SendGridEmailService:
    def send_email(self, recipient: str, subject: str, content: str):
        print("Sending Email through SendGridEmailService")
        print(f"Recipient: {recipient}")
        print(f"Subject: {subject}")
        print(f"Message: {content}")

class OrderService:
    def __init__(self, email_service: NotificationService):
        self.__email_service = email_service

    def create_order(self):
        self.__email_service.send("user@example.com", "Order Created", "Your order has been created successfully.")

email_notification_service = EmailNotificationService()
order_service = OrderService(email_notification_service)
order_service.create_order()

# Infuture, if we want to use SendGridEmailService instead of EmailNotificationService,
#  we can create an adapter class that implements the NotificationService interface and uses the SendGridEmailService to send emails. This way, we can easily switch between different email services without changing the OrderService class.
# But the code fails because SendGridEmailService does not implement the NotificationService interface. We need to create an adapter class that implements the NotificationService interface and uses the SendGridEmailService to send emails.
# And also if it inherits it has send_email method instead of send method. 
# so WE CAN USE AN ADAPTER CLASS