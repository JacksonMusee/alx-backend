#!/usr/bin/env python3
'''
Copy index_range from the previous task and the following class into your code

Implement a method named get_page that takes two integer arguments page with
default value 1 and page_size with default value 10.
'''
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple:
    '''
    Does as above
    '''
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


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
        """
        Fetch a given page
        """

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)

        data = self.dataset()

        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Same as get_page and returns a dictionary containing key-value pairs
        (Hyper media pagination).
        """
        data_set = self.dataset()
        data = self.get_page(page, page_size)

        response = {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if math.ceil(len(data_set) / page_size) > page else None,
            "prev_page": None if page == 1 else page - 1,
            "total_pages": math.ceil(len(data_set) / page_size)
        }

        return response
