#!/usr/bin/python3
"""MRU Cache class"""
from base_caching import BaseCaching
from typing import OrderedDict


class MRUCache(BaseCaching):
    """MRU Cache"""
    def __init__(self):
        """Init"""
        super().__init__()
        self.mru_list = OrderedDict()

    def put(self, key, item):
        """Add Values"""
        if not key or not item:
            return

        self.mru_list[key] = item
        self.cache_data[key] = item

        if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
            remove = next(iter(self.mru_list))
            del self.cache_data[remove]
            print(f"DISCARD: {remove}")

        if len(self.mru_list) > BaseCaching.MAX_ITEMS:
            self.mru_list.popitem(last=False)

        self.mru_list.move_to_end(key, last=False)

    def get(self, key):
        """Get values"""
        if key in self.cache_data:
            self.mru_list.move_to_end(key, last=False)
            return self.cache_data.get(key)
        return None
