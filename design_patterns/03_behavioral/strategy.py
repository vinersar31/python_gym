"""
# Design Pattern: Strategy (Behavioral)

## Intent
Defines a family of algorithms, encapsulates each one, and makes them interchangeable.
Strategy lets the algorithm vary independently from clients that use it.

## Use Cases
- Payment calculation & discounts (Percentage Discount, Flat Coupon, Buy-One-Get-One).
- Navigation routing (Fastest, Shortest, Avoid Tolls, Walking, Transit).
- Compression & Serialization strategies (Gzip, Snappy, JSON, Protobuf).
"""

from abc import ABC, abstractmethod
from typing import List


# 1. Strategy Interface
class DiscountStrategy(ABC):
    @abstractmethod
    def calculate_total(self, raw_total: float) -> float:
        pass


# 2. Concrete Strategies
class NoDiscountStrategy(DiscountStrategy):
    def calculate_total(self, raw_total: float) -> float:
        return raw_total


class PercentageDiscountStrategy(DiscountStrategy):
    def __init__(self, percent: float):
        self._percent = percent  # e.g., 0.15 for 15%

    def calculate_total(self, raw_total: float) -> float:
        return raw_total * (1.0 - self._percent)


class FlatDiscountStrategy(DiscountStrategy):
    def __init__(self, discount_amount: float, minimum_spend: float = 0.0):
        self._discount = discount_amount
        self._minimum_spend = minimum_spend

    def calculate_total(self, raw_total: float) -> float:
        if raw_total >= self._minimum_spend:
            return max(0.0, raw_total - self._discount)
        return raw_total


class VIPLoyaltyStrategy(DiscountStrategy):
    def calculate_total(self, raw_total: float) -> float:
        # 20% discount plus extra $10 off
        return max(0.0, (raw_total * 0.80) - 10.0)


# 3. Context
class ShoppingCart:
    def __init__(self, discount_strategy: DiscountStrategy = NoDiscountStrategy()):
        self._items: List[float] = []
        self._strategy = discount_strategy

    def set_discount_strategy(self, strategy: DiscountStrategy):
        self._strategy = strategy

    def add_item(self, price: float):
        self._items.append(price)

    def get_final_total(self) -> float:
        raw_total = sum(self._items)
        return round(self._strategy.calculate_total(raw_total), 2)


# =====================================================================
# Tests
# =====================================================================
def test_strategy_pattern():
    cart = ShoppingCart()
    cart.add_item(100.0)
    cart.add_item(50.0)
    # Total = 150.0

    # 1. No discount
    assert cart.get_final_total() == 150.0

    # 2. 10% percentage discount -> 135.0
    cart.set_discount_strategy(PercentageDiscountStrategy(0.10))
    assert cart.get_final_total() == 135.0

    # 3. Flat $30 discount for spend >= $100 -> 120.0
    cart.set_discount_strategy(FlatDiscountStrategy(discount_amount=30.0, minimum_spend=100.0))
    assert cart.get_final_total() == 120.0

    # 4. VIP Loyalty (150 * 0.80 - 10) = 110.0
    cart.set_discount_strategy(VIPLoyaltyStrategy())
    assert cart.get_final_total() == 110.0


if __name__ == "__main__":
    test_strategy_pattern()
    print("Strategy pattern tests passed successfully! [OK]")
