"""
# Design Pattern: Facade (Structural)

## Intent
Provides a unified interface to a set of interfaces in a subsystem.
Facade defines a higher-level interface that makes the subsystem easier to use.

## Use Cases
- Complex video/audio encoding conversions (FFmpeg wrappers).
- E-commerce order checkout (Inventory, Payment, Shipping, Notification subsystems).
- Smart home master controller.
"""


# Subsystem 1: Inventory Management
class InventoryService:
    def check_stock(self, item_id: str) -> bool:
        return True

    def reserve(self, item_id: str, quantity: int) -> str:
        return f"Reserved {quantity} units of {item_id}"


# Subsystem 2: Payment Processing
class PaymentGateway:
    def charge(self, user_id: str, amount: float) -> str:
        return f"Charged ${amount:.2f} to user {user_id}"


# Subsystem 3: Logistics & Shipping
class ShippingService:
    def create_shipping_label(self, user_id: str, address: str) -> str:
        return f"Created UPS tracking #TRK-98765 for {address}"


# Subsystem 4: Notification
class EmailService:
    def send_confirmation(self, email: str, order_id: str) -> str:
        return f"Order confirmation {order_id} sent to {email}"


# Facade
class OrderProcessingFacade:
    """Provides a simple checkout() method hiding complex subsystem interactions."""

    def __init__(self):
        self._inventory = InventoryService()
        self._payment = PaymentGateway()
        self._shipping = ShippingService()
        self._notification = EmailService()

    def checkout(
        self, user_id: str, email: str, item_id: str, quantity: int, amount: float, address: str
    ) -> dict:
        if not self._inventory.check_stock(item_id):
            return {"status": "FAILED", "reason": "Out of stock"}

        inv_res = self._inventory.reserve(item_id, quantity)
        pay_res = self._payment.charge(user_id, amount)
        ship_res = self._shipping.create_shipping_label(user_id, address)
        email_res = self._notification.send_confirmation(email, "ORD-12345")

        return {
            "status": "SUCCESS",
            "order_id": "ORD-12345",
            "logs": [inv_res, pay_res, ship_res, email_res],
        }


# =====================================================================
# Tests
# =====================================================================
def test_facade():
    order_facade = OrderProcessingFacade()
    result = order_facade.checkout(
        user_id="usr_42",
        email="customer@example.com",
        item_id="prod_keyboard",
        quantity=1,
        amount=89.99,
        address="123 Main St, New York, NY",
    )

    assert result["status"] == "SUCCESS"
    assert result["order_id"] == "ORD-12345"
    assert len(result["logs"]) == 4


if __name__ == "__main__":
    test_facade()
    print("Facade tests passed successfully! [OK]")
