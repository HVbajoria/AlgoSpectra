from .bubble_sort import BubbleSort
from .insertion_sort import InsertionSort
from .selection_sort import SelectionSort
from .merge_sort import MergeSort
from .quick_sort import QuickSort

import constants as c
class SortFactory:
    @staticmethod
    def get_object(algorithm_name: str) -> object:

        if algorithm_name == c.BUBBLE_SORT:
            return BubbleSort() 
        elif algorithm_name == c.INSERTION_SORT:
            return InsertionSort()
        elif algorithm_name == c.SELECTION_SORT:
            return SelectionSort()
        elif algorithm_name == c.MERGE_SORT:
            return MergeSort()
        elif algorithm_name == c.QUICK_SORT:
            return QuickSort()
        else:
            raise ValueError(f"Algorithm type {algorithm_name} not recognized!")
        