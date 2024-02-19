from .interface import SortInterface
from typing import Callable, List, Optional

class SelectionSort(SortInterface):
    """
    SelectionSort class implementing the selection sort algorithm.

    Inherits from the SortInterface.
    """

    def sort(self, array: List[int], callback: Optional[Callable[[List[int]], None]] = None) -> None:
        """
        Sorts the provided array in-place using the selection sort algorithm.

        Parameters:
        - array (List[int]): The array of integers to be sorted.
        - callback (Optional[Callable[[List[int]], None]]): An optional callback function that gets called 
          after every significant operation (like a swap). Useful for visualization.

        Returns:
        None
        """
        for i in range(len(array)):
            # Find the minimum element's index in the remaining unsorted subarray
            min_idx = i
            for j in range(i + 1, len(array)):
                if array[min_idx] > array[j]:
                    min_idx = j

            # Swap the found minimum element with the first element of the considered subarray
            array[i], array[min_idx] = array[min_idx], array[i]
            if callback:
                callback(array)


    def display_bars(self, array):
        from utils import display_bar_chart
        display_bar_chart(array, is_initial=False)