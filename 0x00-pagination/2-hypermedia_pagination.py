#!/usr/bin/env python3
import csv
import math
from typing import List, Tuple, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get pagination page"""
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0
        size = len(self.dataset())
        start, end = index_range(page, page_size)
        # end = min(end, size)
        if (start > size):
            return []

        return self.dataset()[start: end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        "Get hyper func"
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0

        total_pages = math.ceil(len(self.dataset()) / page_size)

        dict = {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": page + 1 if page + 1 <= total_pages else None,
            "prev_page": page - 1 if page - 1 > 1 else None,
            "total_pages": total_pages
        }

        return dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Helper Function"""
    start = (page - 1) * page_size
    end = page * page_size

    return (start, end)
