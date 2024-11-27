#!/usr/bin/python3
""" BasicCache module
"""


class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError(
            "put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError(
            "get must be implemented in your cache class")


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