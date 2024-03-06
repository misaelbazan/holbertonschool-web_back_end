#!/usr/bin/env python3
"""This module contains a pagination function
"""


from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple:
    """This function takes two arguments
    Args:
        page: int - the page number to retrieve
        page_size: int - limit, specifies the number of items
            that should be returned in a single page
    Returns:
        A tuple containing the start index and the end index
    """
    start_index = (page - 1) * page_size 
    end_index = start_index + page_size
    return (start_index, end_index)