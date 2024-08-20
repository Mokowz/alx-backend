#!/usr/bin/python3
"""LIFO Cache class"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Cache"""
    def __init__(self):
        """Init"""
        super().__init__()
        self.indexes = []

    def put(self, key, item):
        """Add Values"""
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return key

            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS):
                remove = self.indexes.pop(-1)
                del self.cache_data[remove]
                print(f"DISCARD: {remove}")

            self.cache_data[key] = item
            self.indexes.append(key)

    def get(self, key):
        """Get values"""
        if key is None:
            return None
        return self.cache_data.get(key)
