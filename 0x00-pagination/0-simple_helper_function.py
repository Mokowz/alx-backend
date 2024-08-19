#!/usr/bin/env python3
"Pagination using a helper function"
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """Helper Function"""
    start = (page - 1) * page_size
    end = page * page_size

    return (start, end)
