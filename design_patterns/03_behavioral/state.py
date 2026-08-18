"""
# Design Pattern: State (Behavioral)

## Intent
Allows an object to alter its behavior when its internal state changes.
The object will appear to change its class.

## Use Cases
- E-commerce order lifecycle (New -> Paid -> Shipped -> Delivered -> Cancelled).
- Vending machine state management (Idle -> HasCoin -> Dispensing -> SoldOut).
- Document approval workflow (Draft -> UnderReview -> Published).
"""

from abc import ABC, abstractmethod


# 1. Context Interface
class OrderContext:
    def __init__(self):
        self._state = NewOrderState()

    def set_state(self, state: "OrderState"):
        self._state = state

    def pay(self) -> str:
        return self._state.pay(self)

    def ship(self) -> str:
        return self._state.ship(self)

    def deliver(self) -> str:
        return self._state.deliver(self)

    def cancel(self) -> str:
        return self._state.cancel(self)


# 2. State Interface
class OrderState(ABC):
    @abstractmethod
    def pay(self, order: OrderContext) -> str:
        pass

    @abstractmethod
    def ship(self, order: OrderContext) -> str:
        pass

    @abstractmethod
    def deliver(self, order: OrderContext) -> str:
        pass

    @abstractmethod
    def cancel(self, order: OrderContext) -> str:
        pass


# 3. Concrete States
class NewOrderState(OrderState):
    def pay(self, order: OrderContext) -> str:
        order.set_state(PaidOrderState())
        return "Payment processed successfully. State transitioned to PAID."

    def ship(self, order: OrderContext) -> str:
        return "Cannot ship an unpaid order."

    def deliver(self, order: OrderContext) -> str:
        return "Cannot deliver an unpaid order."

    def cancel(self, order: OrderContext) -> str:
        order.set_state(CancelledOrderState())
        return "Order cancelled."


class PaidOrderState(OrderState):
    def pay(self, order: OrderContext) -> str:
        return "Order is already paid."

    def ship(self, order: OrderContext) -> str:
        order.set_state(ShippedOrderState())
        return "Order dispatched for delivery. State transitioned to SHIPPED."

    def deliver(self, order: OrderContext) -> str:
        return "Cannot deliver an order before shipping."

    def cancel(self, order: OrderContext) -> str:
        order.set_state(CancelledOrderState())
        return "Order cancelled and refund initiated."


class ShippedOrderState(OrderState):
    def pay(self, order: OrderContext) -> str:
        return "Order is already paid and shipped."

    def ship(self, order: OrderContext) -> str:
        return "Order is already in transit."

    def deliver(self, order: OrderContext) -> str:
        order.set_state(DeliveredOrderState())
        return "Order delivered successfully. State transitioned to DELIVERED."

    def cancel(self, order: OrderContext) -> str:
        return "Cannot cancel an order that is already in transit."


class DeliveredOrderState(OrderState):
    def pay(self, order: OrderContext) -> str:
        return "Order is already delivered."

    def ship(self, order: OrderContext) -> str:
        return "Order is already delivered."

    def deliver(self, order: OrderContext) -> str:
        return "Order is already delivered."

    def cancel(self, order: OrderContext) -> str:
        return "Cannot cancel a delivered order. Please request a return."


class CancelledOrderState(OrderState):
    def pay(self, order: OrderContext) -> str:
        return "Cannot pay for a cancelled order."

    def ship(self, order: OrderContext) -> str:
        return "Cannot ship a cancelled order."

    def deliver(self, order: OrderContext) -> str:
        return "Cannot deliver a cancelled order."

    def cancel(self, order: OrderContext) -> str:
        return "Order is already cancelled."


# =====================================================================
# Tests
# =====================================================================
def test_state_pattern():
    order = OrderContext()

    # Try invalid transitions
    assert order.ship() == "Cannot ship an unpaid order."

    # Pay -> Paid
    assert "PAID" in order.pay()

    # Ship -> Shipped
    assert "SHIPPED" in order.ship()
    assert order.cancel() == "Cannot cancel an order that is already in transit."

    # Deliver -> Delivered
    assert "DELIVERED" in order.deliver()
    assert order.pay() == "Order is already delivered."


if __name__ == "__main__":
    test_state_pattern()
    print("State pattern tests passed successfully! [OK]")
