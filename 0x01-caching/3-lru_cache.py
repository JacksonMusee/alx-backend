#!/usr/bin/env python3
"""LRU cache module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU cache class
    """

    def __init__(self):
        """Initialize
        """
        super().__init__()

    def put(self, key, item):
        """Add items to cache
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                least_used_item_key = next(iter(self.cache_data))
                self.cache_data.pop(least_used_item_key)
                print(f"DISCARD: {least_used_item_key}")

            self.cache_data[key] = item

    def get(self, key):
        """Retrieves a record from cache
        """
        if not key:
            return None

        result = self.cache_data.get(key)

        if result:
            poped_key, poped_value = self.cache_data.pop(key)
            self.cache_data[poped_key] = poped_value

        return result
