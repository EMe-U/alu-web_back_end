#!/usr/bin/env python3
"""Simple helper function for pagination."""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple of start and end index for pagination.

    Args:
        page: The page number (1-indexed)
        page_size: The number of items per page

    Returns:
        A tuple containing start index and end index
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
