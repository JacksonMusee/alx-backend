#!/usr/bin/env python3
"""LIFO cache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO cache class
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
                poped_item = self.cache_data.pop()
                print(f"DISCARD: {poped_item}")

            self.cache_data[key] = item

    def get(self, key):
        """Retrieves a record from cache
        """
        if not key:
            return None

        return self.cache_data.get(key)
