#!/usr/bin/python3
"""LIFOCache module - LIFO caching system."""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class that inherits from BaseCaching."""

    def __init__(self):
        """Initialize the cache."""
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """Add an item in the cache using LIFO algorithm."""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data:
                if self.last_key is not None:
                    del self.cache_data[self.last_key]
                    print("DISCARD: {}".format(self.last_key))

        self.cache_data[key] = item
        self.last_key = key

    def get(self, key):
        """Get an item by key."""
        if key is None:
            return None
        return self.cache_data.get(key)
