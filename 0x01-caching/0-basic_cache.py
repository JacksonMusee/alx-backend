#!/usr/bin/env python3
""" Basic Cache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ A basic cache with no limit
    """

    def __init__(self):
        """Initialize
        """
        super().__init__()

    def put(self, key, item):
        """Add data to cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves a record from cache
        """
        if not key:
            return None
        return self.cache_data.get(key)
