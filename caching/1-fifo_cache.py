#!/usr/bin/python3
"""FIFOCache module - FIFO caching system."""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class that inherits from BaseCaching."""

    def __init__(self):
        """Initialize the cache."""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item in the cache using FIFO algorithm."""
        if key is None or item is None:
            return

        if key not in self.cache_data:
            self.order.append(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = self.order.pop(0)
            del self.cache_data[first_key]
            print("DISCARD: {}".format(first_key))

    def get(self, key):
        """Get an item by key."""
        if key is None:
            return None
        return self.cache_data.get(key)
