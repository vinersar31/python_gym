"""
# Design Pattern: Decorator (Structural)

## Intent
Attaches additional responsibilities to an object dynamically.
Decorators provide a flexible alternative to subclassing for extending functionality.

## Use Cases
- Beverage / Coffee ordering systems (Milk, Sugar, Whip toppings).
- Stream processing pipelines (Encryption, Compression, Buffering).
- Middleware execution chains.
"""

from abc import ABC, abstractmethod


# 1. Component Interface
class Coffee(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass

    @abstractmethod
    def description(self) -> str:
        pass


# 2. Concrete Base Component
class SimpleCoffee(Coffee):
    def cost(self) -> float:
        return 2.00

    def description(self) -> str:
        return "Simple Coffee"


# 3. Base Decorator
class CoffeeDecorator(Coffee):
    def __init__(self, decorated_coffee: Coffee):
        self._decorated_coffee = decorated_coffee

    def cost(self) -> float:
        return self._decorated_coffee.cost()

    def description(self) -> str:
        return self._decorated_coffee.description()


# 4. Concrete Decorators
class Milk(CoffeeDecorator):
    def cost(self) -> float:
        return self._decorated_coffee.cost() + 0.50

    def description(self) -> str:
        return f"{self._decorated_coffee.description()}, Milk"


class Sugar(CoffeeDecorator):
    def cost(self) -> float:
        return self._decorated_coffee.cost() + 0.25

    def description(self) -> str:
        return f"{self._decorated_coffee.description()}, Sugar"


class VanillaSyrup(CoffeeDecorator):
    def cost(self) -> float:
        return self._decorated_coffee.cost() + 0.75

    def description(self) -> str:
        return f"{self._decorated_coffee.description()}, Vanilla Syrup"


# =====================================================================
# Tests
# =====================================================================
def test_decorator_pattern():
    my_coffee = SimpleCoffee()
    assert my_coffee.cost() == 2.00
    assert my_coffee.description() == "Simple Coffee"

    # Wrap with Milk and Sugar
    my_coffee = Milk(my_coffee)
    my_coffee = Sugar(my_coffee)
    assert my_coffee.cost() == 2.75
    assert my_coffee.description() == "Simple Coffee, Milk, Sugar"

    # Add Vanilla
    my_coffee = VanillaSyrup(my_coffee)
    assert my_coffee.cost() == 3.50
    assert my_coffee.description() == "Simple Coffee, Milk, Sugar, Vanilla Syrup"


if __name__ == "__main__":
    test_decorator_pattern()
    print("Decorator pattern tests passed successfully! [OK]")
