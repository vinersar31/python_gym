"""
# Design Pattern: Singleton (Creational)

## Intent
Ensures a class has only one instance, and provides a global point of access to it.

## Python Implementations Covered:
1. Thread-safe Metaclass approach (recommended for OOP architectures).
2. `__new__` override approach.
3. Module-level singleton (the most idiomatic Python approach).
"""

import threading
from typing import Any, Dict


# 1. Thread-Safe Metaclass Singleton
class SingletonMeta(type):
    """
    Thread-safe implementation of Singleton pattern via Metaclass.
    """

    _instances: Dict[type, Any] = {}
    _lock: threading.Lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class DatabaseConnectionPool(metaclass=SingletonMeta):
    def __init__(self, host: str = "localhost", max_connections: int = 10):
        # Prevent re-initialization if already created
        if not hasattr(self, "_initialized"):
            self.host = host
            self.max_connections = max_connections
            self._initialized = True

    def query(self, sql: str) -> str:
        return f"Executing '{sql}' on connection pool ({self.host})"


# 2. __new__ Based Singleton
class AppConfig:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(AppConfig, cls).__new__(cls)
                cls._instance.settings = {}
        return cls._instance

    def set(self, key: str, value: Any):
        self.settings[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        return self.settings.get(key, default)


# =====================================================================
# Tests
# =====================================================================
def test_singleton_metaclass():
    pool1 = DatabaseConnectionPool("db.production.internal", 20)
    pool2 = DatabaseConnectionPool("different.host", 50)

    assert pool1 is pool2
    assert pool1.host == "db.production.internal"  # Kept original init


def test_singleton_new():
    config1 = AppConfig()
    config1.set("DEBUG", True)

    config2 = AppConfig()
    assert config2.get("DEBUG") is True
    assert config1 is config2


if __name__ == "__main__":
    test_singleton_metaclass()
    test_singleton_new()
    print("Singleton tests passed successfully! [OK]")
