"""
# Low-Level Design: LFU Cache (Least Frequently Used)

## Requirements
- `get(key)`: Retrieve value in O(1) time and increment its access count.
- `put(key, value)`: Insert/update value in O(1). If capacity is exceeded, evict the least frequently used key. If there is a tie, evict the least recently used key among them.

## Data Structure
- `cache`: Dict[key -> (value, frequency)]
- `freq_to_keys`: Dict[frequency -> OrderedDict(key -> None)]
- `min_freq`: integer tracking the current minimum frequency in the cache.
"""

from collections import defaultdict, OrderedDict


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_val_freq = {}  # key -> [val, freq]
        self.freq_to_keys = defaultdict(OrderedDict)  # freq -> OrderedDict of keys

    def _update_freq(self, key: int):
        val, freq = self.key_to_val_freq[key]
        del self.freq_to_keys[freq][key]

        # If this frequency bucket is now empty and was the min_freq, increment min_freq
        if not self.freq_to_keys[freq] and self.min_freq == freq:
            self.min_freq += 1

        new_freq = freq + 1
        self.key_to_val_freq[key][1] = new_freq
        self.freq_to_keys[new_freq][key] = None

    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1
        self._update_freq(key)
        return self.key_to_val_freq[key][0]

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        if key in self.key_to_val_freq:
            self.key_to_val_freq[key][0] = value
            self._update_freq(key)
            return

        if len(self.key_to_val_freq) >= self.capacity:
            # Evict least frequently used key (first item in min_freq OrderedDict)
            evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val_freq[evict_key]

        # Insert new key with freq = 1
        self.key_to_val_freq[key] = [value, 1]
        self.freq_to_keys[1][key] = None
        self.min_freq = 1


# =====================================================================
# Tests
# =====================================================================
def test_lfu_cache():
    lfu = LFUCache(2)
    lfu.put(1, 1)
    lfu.put(2, 2)
    assert lfu.get(1) == 1        # freq of 1 is 2
    lfu.put(3, 3)                 # evicts key 2 (freq of 2 was 1, freq of 1 was 2)
    assert lfu.get(2) == -1       # not found
    assert lfu.get(3) == 3        # freq of 3 is 2
    lfu.put(4, 4)                 # both 1 and 3 have freq 2. Key 1 is LRU, so 1 is evicted!
    assert lfu.get(1) == -1       # not found
    assert lfu.get(3) == 3
    assert lfu.get(4) == 4


if __name__ == "__main__":
    test_lfu_cache()
    print("LFU Cache LLD tests passed successfully! [OK]")
