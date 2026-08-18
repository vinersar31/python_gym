"""
# Design Pattern: Factory Method (Creational)

## Intent
Defines an interface for creating an object, but lets subclasses decide which class to instantiate.
Factory Method lets a class defer instantiation to subclasses.

## Use Cases
- When a class cannot anticipate the class of objects it must create.
- When a class wants its subclasses to specify the objects it creates.
- Decoupling payment gateways (Stripe, PayPal, Crypto), notification dispatchers (Email, SMS, Push), or file parsers (JSON, XML, CSV).
"""

from abc import ABC, abstractmethod


# 1. Product Interface
class Notification(ABC):
    @abstractmethod
    def send(self, recipient: str, message: str) -> str:
        """Send notification to recipient."""
        pass


# 2. Concrete Products
class EmailNotification(Notification):
    def send(self, recipient: str, message: str) -> str:
        return f"Sending Email to {recipient}: '{message}' via SMTP Server"


class SMSNotification(Notification):
    def send(self, recipient: str, message: str) -> str:
        return f"Sending SMS to {recipient}: '{message}' via Twilio Gateway"


class PushNotification(Notification):
    def send(self, recipient: str, message: str) -> str:
        return f"Sending Push Notification to {recipient}: '{message}' via Firebase Cloud Messaging"


# 3. Creator / Factory Interface
class NotificationFactory(ABC):
    @abstractmethod
    def create_notification(self) -> Notification:
        """Factory Method to be implemented by concrete creators."""
        pass

    def notify(self, recipient: str, message: str) -> str:
        """Core business logic that relies on the product produced by the factory method."""
        notification = self.create_notification()
        return notification.send(recipient, message)


# 4. Concrete Creators
class EmailNotificationFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return EmailNotification()


class SMSNotificationFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return SMSNotification()


class PushNotificationFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return PushNotification()


# =====================================================================
# Tests
# =====================================================================
def test_factory_method():
    email_factory = EmailNotificationFactory()
    res_email = email_factory.notify("user@example.com", "Your order has shipped")
    assert "Sending Email to user@example.com" in res_email
    assert "SMTP" in res_email

    sms_factory = SMSNotificationFactory()
    res_sms = sms_factory.notify("+1234567890", "Your 2FA code is 123456")
    assert "Sending SMS to +1234567890" in res_sms
    assert "Twilio" in res_sms

    push_factory = PushNotificationFactory()
    res_push = push_factory.notify("device_token_abc", "New direct message")
    assert "Sending Push Notification" in res_push
    assert "Firebase" in res_push


if __name__ == "__main__":
    test_factory_method()
    print("Factory Method tests passed successfully! [OK]")
