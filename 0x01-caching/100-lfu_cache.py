#!/usr/bin/env python3
"""LFU cache module
"""

from collections import defaultdict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU cache class"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.access_frequency = defaultdict(int)
        self.key_order = defaultdict(list)
        self.min_freq = 0

    def _update_frequency(self, key):
        """Helper to update the frequency of a key"""
        old_freq = self.access_frequency[key]
        new_freq = old_freq + 1

        self.access_frequency[key] = new_freq

        self.key_order[new_freq].append(key)

        self.key_order[old_freq].remove(key)

        if not self.key_order[old_freq]:
            del self.key_order[old_freq]
            if old_freq == self.min_freq:
                self.min_freq += 1

    def put(self, key, item):
        """Add items to cache"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            least_freq_key = self.key_order[self.min_freq].pop(0)
            self.cache_data.pop(least_freq_key)
            self.access_frequency.pop(least_freq_key)
            print(f"DISCARD: {least_freq_key}")

        self.cache_data[key] = item
        self.access_frequency[key] = 1
        self.key_order[1].append(key)
        self.min_freq = 1

    def get(self, key):
        """Retrieves a record from cache"""
        if key is None or key not in self.cache_data:
            return None

        self._update_frequency(key)

        return self.cache_data[key]
