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

class SendGridAdapter(NotificationService):
    def __init__(self, sendgrid_service: SendGridEmailService):
        self.__sendgrid_service = sendgrid_service

    # Client Only sees the send Method 
    def send(self, to: str, title: str, body: str):
        self.__sendgrid_service.send_email(to, title, body)
    

# Here the client is Order Service class which is dependent on the NotificationService interface.
# It does not need to have different methods for different email services. It can use the same send method to send emails through different email services.
# Use of the adapter pattern allows us to use different email services without changing the OrderService class. We can easily switch between different email services by creating an adapter class that implements the NotificationService interface and uses the specific email service to send emails.
class OrderService:
    def __init__(self, email_service: NotificationService):
        self.__email_service = email_service

    def create_order(self):
        self.__email_service.send("user@example.com", "Order Created", "Your order has been created successfully.")

# email_notification_service = EmailNotificationService()
# order_service = OrderService(email_notification_service)
# order_service.create_order()

senddgrid_email_service = SendGridEmailService()
sendgrid_adapter = SendGridAdapter(senddgrid_email_service)
order_service = OrderService(sendgrid_adapter)
order_service.create_order()