#!/usr/bin/python3
"""LRU Cache class"""
from base_caching import BaseCaching
from typing import OrderedDict


class LRUCache(BaseCaching):
    """LRU Cache"""
    def __init__(self):
        """Init"""
        super().__init__()
        self.lru_list = OrderedDict()

    def put(self, key, item):
        """Add Values"""
        if key and item:
            self.lru_list[key] = item
            self.lru_list.move_to_end(key)
            self.cache_data[key] = item

            if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
                remove = next(iter(self.lru_list))
                del self.cache_data[remove]
                print(f"DISCARD: {remove}")

            if len(self.lru_list) > BaseCaching.MAX_ITEMS:
                self.lru_list.popitem(last=False)

    def get(self, key):
        """Get values"""
        if key in self.cache_data:
            self.lru_list.move_to_end(key)
            return self.cache_data.get(key)
        return None
