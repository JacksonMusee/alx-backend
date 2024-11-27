#!/usr/bin/env python3
"""LFU cache module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU cache class
    """

    def __init__(self):
        """Initialize
        """
        super().__init__()
        self.access_frequency = {}

    def sort(self):
        """Sorts access_frequency in ascending order
        """
        sorted_frequency = sorted(
            self.access_frequency.items(), key=lambda x: x[1])
        self.access_frequency = dict(sorted_frequency)

    def put(self, key, item):
        """Add items to cache
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_item = next(iter(self.access_frequency))
                min_frequency = self.access_frequency[first_item]

                to_discard = [
                    key for key, value in self.access_frequency.items() if value == min_frequency]

                for key, _ in self.access_frequency.items():
                    if key in to_discard:
                        least_used_item_key = key
                        break

                least_used_item_key = next(iter(self.cache_data))
                self.cache_data.pop(least_used_item_key)
                self.access_frequency.pop(least_used_item_key)
                print(f"DISCARD: {least_used_item_key}")

            self.cache_data[key] = item
            self.access_frequency[key] = 1
            self.sort()

    def get(self, key):
        """Retrieves a record from cache
        """
        if not key:
            return None

        result = self.cache_data.get(key)

        if result:
            poped_value = self.cache_data.pop(key)
            self.cache_data[key] = poped_value
            self.access_frequency[key] += 1
            self.sort()

        return result
