"""
# Low-Level Design: In-Memory Key-Value Store with Nested Transactions

## Requirements
- `set(key, value)`: Store key-value pair.
- `get(key)`: Retrieve value.
- `delete(key)`: Delete key.
- `begin()`: Open a new transaction level.
- `commit()`: Persist all updates in the active transaction(s).
- `rollback()`: Revert all changes in the current active transaction.
"""

from typing import Dict, List, Optional, Any


class TransactionalKVStore:
    def __init__(self):
        # Global storage
        self._global_store: Dict[str, Any] = {}
        # Transaction stack. Each element is a dict tracking original state before modification
        # None value in transaction diff indicates the key was newly added in that transaction
        self._transaction_stack: List[Dict[str, Optional[Any]]] = []

    def get(self, key: str) -> Optional[Any]:
        return self._global_store.get(key)

    def set(self, key: str, value: Any):
        if self._transaction_stack:
            curr_tx = self._transaction_stack[-1]
            if key not in curr_tx:
                # Record initial state before overwrite (None if didn't exist)
                curr_tx[key] = self._global_store.get(key)

        self._global_store[key] = value

    def delete(self, key: str) -> bool:
        if key not in self._global_store:
            return False

        if self._transaction_stack:
            curr_tx = self._transaction_stack[-1]
            if key not in curr_tx:
                curr_tx[key] = self._global_store.get(key)

        del self._global_store[key]
        return True

    def begin(self):
        """Start a new nested transaction."""
        self._transaction_stack.append({})

    def rollback(self) -> bool:
        """Rollback changes made in current transaction."""
        if not self._transaction_stack:
            return False

        tx = self._transaction_stack.pop()
        for key, original_val in tx.items():
            if original_val is None:
                # Key was added in this transaction, remove it
                self._global_store.pop(key, None)
            else:
                # Key was modified or deleted, restore original value
                self._global_store[key] = original_val
        return True

    def commit(self) -> bool:
        """Commit all transactions."""
        if not self._transaction_stack:
            return False
        # Clear transaction history, all changes are now permanent
        self._transaction_stack.clear()
        return True


# =====================================================================
# Tests
# =====================================================================
def test_transactional_kv_store():
    store = TransactionalKVStore()
    store.set("a", 10)
    assert store.get("a") == 10

    # 1. Begin transaction 1
    store.begin()
    store.set("a", 20)
    store.set("b", 30)
    assert store.get("a") == 20
    assert store.get("b") == 30

    # 2. Begin nested transaction 2
    store.begin()
    store.set("a", 99)
    store.delete("b")
    assert store.get("a") == 99
    assert store.get("b") is None

    # 3. Rollback transaction 2 -> restores Tx 1 state
    assert store.rollback() is True
    assert store.get("a") == 20
    assert store.get("b") == 30

    # 4. Commit transaction 1 -> makes state permanent
    assert store.commit() is True
    assert store.get("a") == 20
    assert store.get("b") == 30

    # 5. Cannot rollback after commit
    assert store.rollback() is False


if __name__ == "__main__":
    test_transactional_kv_store()
    print("Transactional KV Store LLD tests passed successfully! [OK]")
