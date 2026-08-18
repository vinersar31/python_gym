"""
# Design Pattern: Observer (Behavioral)

## Intent
Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

## Use Cases
- Event-driven pub-sub systems.
- Stock market ticker updates / Price alerts.
- Reactive UI event binding.
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any


# 1. Observer Interface (Subscriber)
class Observer(ABC):
    @abstractmethod
    def update(self, event_type: str, data: Any):
        pass


# 2. Subject Interface (Publisher)
class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self, event_type: str, data: Any):
        pass


# 3. Concrete Subject (Stock Market Ticker)
class StockTicker(Subject):
    def __init__(self, symbol: str):
        self.symbol = symbol
        self._price: float = 0.0
        self._observers: List[Observer] = []

    def attach(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, event_type: str, data: Any):
        for observer in self._observers:
            observer.update(event_type, data)

    def set_price(self, new_price: float):
        old_price = self._price
        self._price = new_price
        self.notify(
            "PRICE_CHANGE",
            {"symbol": self.symbol, "old_price": old_price, "new_price": new_price},
        )


# 4. Concrete Observers
class TraderAlertBot(Observer):
    def __init__(self, name: str, threshold: float):
        self.name = name
        self.threshold = threshold
        self.alerts: List[str] = []

    def update(self, event_type: str, data: Any):
        if event_type == "PRICE_CHANGE" and data["new_price"] >= self.threshold:
            msg = f"Alert for {self.name}: {data['symbol']} exceeded threshold {self.threshold} (Now: {data['new_price']})"
            self.alerts.append(msg)


class AuditLogger(Observer):
    def __init__(self):
        self.logs: List[str] = []

    def update(self, event_type: str, data: Any):
        self.logs.append(f"Event: {event_type} | Data: {data}")


# =====================================================================
# Tests
# =====================================================================
def test_observer_pattern():
    nvda = StockTicker("NVDA")
    bot = TraderAlertBot("AlphaBot", threshold=120.0)
    logger = AuditLogger()

    nvda.attach(bot)
    nvda.attach(logger)

    # Price update 1: 110 (below bot threshold)
    nvda.set_price(110.0)
    assert len(bot.alerts) == 0
    assert len(logger.logs) == 1

    # Price update 2: 125 (above bot threshold)
    nvda.set_price(125.0)
    assert len(bot.alerts) == 1
    assert "NVDA exceeded threshold 120.0" in bot.alerts[0]
    assert len(logger.logs) == 2

    # Detach bot
    nvda.detach(bot)
    nvda.set_price(130.0)
    assert len(bot.alerts) == 1  # No new alerts


if __name__ == "__main__":
    test_observer_pattern()
    print("Observer pattern tests passed successfully! [OK]")
