"""
# Design Pattern: Proxy (Structural)

## Intent
Provides a surrogate or placeholder for another object to control access to it.

## Types of Proxies:
1. **Virtual Proxy (Lazy Loading)**: Defers creation of resource-intensive objects until needed.
2. **Protection Proxy (Access Control)**: Restricts access based on user permissions.
3. **Caching Proxy**: Caches expensive operation results.
"""

from abc import ABC, abstractmethod
import time


# 1. Subject Interface
class DatabaseReader(ABC):
    @abstractmethod
    def get_user_data(self, user_id: str) -> dict:
        pass


# 2. Real Subject (Expensive database operation)
class RealDatabaseReader(DatabaseReader):
    def __init__(self):
        # Simulating heavy connection overhead
        self._connected = True

    def get_user_data(self, user_id: str) -> dict:
        # In real life, queries a remote database
        return {"user_id": user_id, "name": f"User_{user_id}", "plan": "Premium"}


# 3. Caching & Protection Proxy
class CachedSecureDatabaseProxy(DatabaseReader):
    def __init__(self, current_user_role: str):
        self._role = current_user_role
        self._real_reader = None  # Lazy initialization
        self._cache = {}

    def _get_real_reader(self) -> RealDatabaseReader:
        if self._real_reader is None:
            self._real_reader = RealDatabaseReader()
        return self._real_reader

    def get_user_data(self, user_id: str) -> dict:
        # Protection Check
        if self._role not in ("admin", "auditor", "manager"):
            raise PermissionError(f"Role '{self._role}' is unauthorized to read user data")

        # Cache Check
        if user_id in self._cache:
            return {"data": self._cache[user_id], "source": "CACHE"}

        # Fetch from Real Database
        data = self._get_real_reader().get_user_data(user_id)
        self._cache[user_id] = data
        return {"data": data, "source": "DATABASE"}


# =====================================================================
# Tests
# =====================================================================
def test_proxy():
    admin_proxy = CachedSecureDatabaseProxy("admin")

    # 1. First fetch hits DB
    res1 = admin_proxy.get_user_data("usr_100")
    assert res1["source"] == "DATABASE"
    assert res1["data"]["user_id"] == "usr_100"

    # 2. Second fetch hits Cache
    res2 = admin_proxy.get_user_data("usr_100")
    assert res2["source"] == "CACHE"

    # 3. Unauthorized access raises PermissionError
    guest_proxy = CachedSecureDatabaseProxy("guest")
    try:
        guest_proxy.get_user_data("usr_100")
        assert False, "Expected PermissionError"
    except PermissionError:
        pass


if __name__ == "__main__":
    test_proxy()
    print("Proxy tests passed successfully! [OK]")
