#!/usr/bin/env python3
"""FIFO cache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO cache class
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
                first_item = next(iter(self.cache_data))
                self.cache_data.pop(first_item)
                print(f"DISCARD: {first_item}")

            self.cache_data[key] = item

    def get(self, key):
        """Retrieves a record from cache
        """
        if not key:
            return None

        return self.cache_data.get(key)
