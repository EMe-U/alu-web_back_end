#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination."""

import csv
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the Server instance."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset.

        Returns:
            The dataset as a list of lists
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0.

        Returns:
            The indexed dataset as a dictionary
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Get deletion-resilient hypermedia pagination info.

        Args:
            index: The start index for pagination
            page_size: The number of items per page

        Returns:
            A dictionary with pagination metadata resilient to deletions
        """
        indexed_data = self.indexed_dataset()

        assert index is not None and 0 <= index < len(self.dataset())

        data = []
        current_index = index
        items_collected = 0
        dataset_len = len(self.dataset())

        while items_collected < page_size and current_index < dataset_len:
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
                items_collected += 1
            current_index += 1

        next_index = current_index

        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index
        }
