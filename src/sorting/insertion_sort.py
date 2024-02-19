from typing import List, Callable, Optional
from .interface import SortInterface

class InsertionSort(SortInterface):

    def sort(self, array: List[int], callback: Optional[Callable[[List[int]], None]] = None) -> None:
        """
        Sorts the given list using the Insertion Sort algorithm.

        Parameters:
        - array (List[int]): The list of integers to be sorted.
        - callback (Optional[Callable[[List[int]], None]]): A callback function that gets called on every shift.
        """
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1

            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1

                if callback:
                    callback(array)
                    
            array[j + 1] = key
    
    def display_bars(self, array: List[int]) -> None:
        """
        Display the bars representation of the list.

        Parameters:
        - array (List[int]): The list of integers to be displayed.
        """
        from utils import display_bar_chart
        display_bar_chart(array, is_initial=False)