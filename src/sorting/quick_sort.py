from .interface import SortInterface
from typing import Callable, List, Optional

class QuickSort(SortInterface):
    def __init__(self) -> None:
        pass

    def _partition(self, array: List[int], low: int, high: int, callback: Optional[Callable[[List[int]], None]]) -> int:
        """
        Private helper method for quicksort. This method selects a pivot and partitions the array 
        around the pivot such that elements smaller than the pivot are on the left and 
        elements greater than the pivot are on the right.

        Parameters:
        - array (List[int]): The array of integers to be partitioned.
        - low (int): The starting index for the partition.
        - high (int): The ending index for the partition.
        - callback (Optional[Callable[[List[int]], None]]): An optional callback function for visualization.

        Returns:
        int: The index of the pivot after partitioning.
        """
        pivot = array[high]
        i = low - 1

        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
                if callback:
                    callback(array)

        array[i + 1], array[high] = array[high], array[i + 1]
        if callback:
            callback(array)

        return i + 1

    def _quicksort(self, array: List[int], low: int, high: int, callback: Optional[Callable[[List[int]], None]]) -> None:
        """
        Private recursive helper method for the quick sort algorithm.

        Parameters:
        - array (List[int]): The array of integers to be sorted.
        - low (int): The starting index for the sort.
        - high (int): The ending index for the sort.
        - callback (Optional[Callable[[List[int]], None]]): An optional callback function for visualization.

        Returns:
        None
        """
        if low < high:
            pi = self._partition(array, low, high, callback)
            self._quicksort(array, low, pi - 1, callback)
            self._quicksort(array, pi + 1, high, callback)

    def sort(self, array: List[int], callback: Optional[Callable[[List[int]], None]] = None) -> None:
        self._quicksort(array, 0, len(array) - 1, callback)

    def display_bars(self, array):
        from utils import display_bar_chart
        display_bar_chart(array, is_initial=False)