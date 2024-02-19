from typing import List, Callable, Optional, Any
from .interface import SortInterface

class MergeSort(SortInterface):

    def _merge(self, arr: List[int], l: int, m: int, r: int, temp: List[int]) -> None:
        """Helper function to merge two sorted sublists into a single sorted list."""
        # Copy the sublists to a temporary list
        for i in range(l, r + 1):
            temp[i] = arr[i]

        i, j, k = l, m + 1, l

        # Merge the temp lists back into arr[l..r]
        while i <= m and j <= r:
            if temp[i] <= temp[j]:
                arr[k] = temp[i]
                i += 1
            else:
                arr[k] = temp[j]
                j += 1
            k += 1

        # Copy the remaining elements of temp[l..m] (if any)
        while i <= m:
            arr[k] = temp[i]
            i += 1
            k += 1

        # Copy the remaining elements of temp[m+1..r] (if any)
        while j <= r:
            arr[k] = temp[j]
            j += 1
            k += 1

    def _merge_sort(self, arr: List[int], l: int, r: int, temp: List[int], 
                    callback: Optional[Callable[[List[int], List[int]], None]] = None) -> None:
        """Recursive helper function that sorts the input list using the merge sort algorithm."""
        if l < r:
            mid = (l + r) // 2
            
            self._merge_sort(arr, l, mid, temp, callback)
            self._merge_sort(arr, mid + 1, r, temp, callback)
            self._merge(arr, l, mid, r, temp)

            if callback:
                callback(arr, arr[l:r+1])

    def sort(self, array: List[int], 
             callback: Optional[Callable[[List[int], Any], None]] = None) -> None:
        """
        Sorts the given list using the Merge Sort algorithm.

        Parameters:
        - array (List[int]): The list of integers to be sorted.
        - callback (Optional[Callable[[List[int], Any], None]]): A callback function that gets called after each merge.
        """
        temp = [0] * len(array)
        self._merge_sort(array, 0, len(array) - 1, temp, callback)
        if callback:
            callback(array, None)

    def display_bars(self, array: List[int], sub_array: Optional[List[int]] = None) -> None:
        """
        Display the bars representation of the list with a highlighted sub-array.

        Parameters:
        - array (List[int]): The list of integers to be displayed.
        - sub_array (Optional[List[int]]): The sublist of integers to be highlighted.
        """
        from utils import display_bar_chart
        display_bar_chart(array, sub_array, is_merge=True, is_initial=False)s