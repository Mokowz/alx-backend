#!/usr/bin/python3
"""Base Cache class"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic Cache Class"""
    def put(self, key, item):
        """Assign to values cache"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Get values in cache"""
        if (key is None):
            return None
        return self.cache_data.get(key)
