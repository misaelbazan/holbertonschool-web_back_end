#!/usr/bin/env python3
"""This module must be commented
"""

import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
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
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        start, end = index_range(page, page_size)
        try:
            data = self.dataset()
            return data[start:end]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[int, List]:
        """Returns a dictionary containinf the following key-value pairs:
            page_size: int - the length of the returned dataset page
            page: int - the current page number
            data: List - the dataset page (return of get_page())
            next_page: int - number of the next page, None if no next page
            prev_page: int - number of the previous page, None if no
                previous page.
            total_pages: int - the total number of pages in the dataset
        """
        total_items = len(self.dataset())
        total_pages = (
                total_items // page_size +
                (1 if total_items % page_size > 0 else 0)
        )
        data = self.get_page(page, page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        metadata = {}
        metadata["page_size"] = page_size if data else 0
        metadata["page"] = page
        metadata["data"] = data
        metadata["next_page"] = next_page
        metadata["prev_page"] = prev_page
        metadata["total_pages"] = total_pages
        return metadata
