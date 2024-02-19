from typing import List, Callable, Optional
from .interface import SortInterface

class BubbleSort(SortInterface):
    def sort(self, array: List[int], callback: Optional[Callable[[List[int]], None]] = None) -> None:
        """
        Sorts the given list using Bubble Sort algorithm.

        Parameters:
        - array (List[int]): The list of integers to be sorted.
        - callback (Optional[Callable[[List[int]], None]]): A callback function that gets called on every swap.
        """
        n = len(array)
     
        for i in range(n):
            swapped = False
 
            for j in range(0, n-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                    if callback:
                        callback(array)
                    swapped = True

            # If no two elements were swapped in the inner loop, the list is already sorted.
            if not swapped:
                break
    
    def display_bars(self, array: List[int]) -> None:
        """
        Display the bars representation of the list.

        Parameters:
        - array (List[int]): The list of integers to be displayed.
        """
        from utils import display_bar_chart
        display_bar_chart(array, is_initial=False)
        