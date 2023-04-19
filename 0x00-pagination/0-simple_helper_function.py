#!/usr/bin/env python3
""" pagination task"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ give the start of index and the end of index corresponding
        to th ranges of indexesss """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
