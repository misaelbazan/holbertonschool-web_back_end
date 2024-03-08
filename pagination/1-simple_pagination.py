#!/usr/bin/env python3
"""
"""

import csv
import math
from typing import List, Tuple


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize an object"""
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
        """Function to return the filtered content via pagination"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        indexes = index_range(page, page_size)
        try:
            data = self.dataset()
            return data[indexes[0]:indexes[1]]
        except IndexError:
            return []
