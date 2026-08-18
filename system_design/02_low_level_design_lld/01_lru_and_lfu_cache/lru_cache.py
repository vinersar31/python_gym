"""
# Low-Level Design: LRU Cache (Least Recently Used)

## Requirements
- `get(key)`: Retrieve value in O(1) time and mark key as most recently used. Return -1 if not found.
- `put(key, value)`: Insert/update value in O(1). If capacity exceeded, evict the least recently used key.

## Data Structure
- Hash Map (key -> Node) for O(1) lookup.
- Doubly Linked List with dummy head & tail for O(1) insertion, removal, and reordering.
"""

from typing import Optional, Dict


class DNode:
    def __init__(self, key: int = 0, val: int = 0):
        self.key: int = key
        self.val: int = val
        self.prev: Optional["DNode"] = None
        self.next: Optional["DNode"] = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.cache: Dict[int, DNode] = {}
        # Sentinel dummy nodes
        self.head: DNode = DNode()
        self.tail: DNode = DNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: DNode):
        """Remove an existing node from the doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_head(self, node: DNode):
        """Insert a node right after dummy head (most recently used position)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_to_head(node)
        else:
            if len(self.cache) >= self.capacity:
                # Evict least recently used (node right before dummy tail)
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]

            new_node = DNode(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)


# =====================================================================
# Tests
# =====================================================================
def test_lru_cache():
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    assert lru.get(1) == 1       # returns 1, (1 is now MRU, 2 is LRU)
    lru.put(3, 3)                # evicts key 2
    assert lru.get(2) == -1      # returns -1 (not found)
    lru.put(4, 4)                # evicts key 1 (since 3 was put after 1, 1 was LRU)
    assert lru.get(1) == -1      # returns -1 (not found)
    assert lru.get(3) == 3       # returns 3
    assert lru.get(4) == 4       # returns 4


if __name__ == "__main__":
    test_lru_cache()
    print("LRU Cache LLD tests passed successfully! [OK]")
