SEARCHING_ALGORITHM = "Searching Algorithm's"
SORTING_ALGORITHM = "Sorting Algorithm's"

# Sorting algorithms
BUBBLE_SORT = "Bubble Sort"
SELECTION_SORT = "Selection Sort"
INSERTION_SORT = "Insertion Sort"
MERGE_SORT = "Merge Sort"
QUICK_SORT = "Quick Sort"
HEAP_SORT = "Heap Sort"
SHELL_SORT = "Shell Sort"
RADIX_SORT = "Radix Sort"
COUNTING_SORT = "Counting Sort"
BUCKET_SORT = "Bucket Sort"

# Searching algorithms
LINEAR_SEARCH = "Linear Search"
BINARY_SEARCH = "Binary Search"
JUMP_SEARCH = "Jump Search"
INTERPOLATION_SEARCH = "Interpolation Search"
EXPONENTIAL_SEARCH = "Exponential Search"
TERNARY_SEARCH = "Ternary Search"


ALGORITHM_COMPLEXITIES = {
    "Bubble Sort": {
        "Time": "O(n^2)",
        "Best Time": "O(n)",
        "Space": "O(1)"
    },
    "Merge Sort": {
        "Time": "O(n log n)",
        "Best Time": "O(n log n)",
        "Space": "O(n)"
    },
    "Insertion Sort": {
        "Time": "O(n^2)",
        "Best Time": "O(n)",
        "Space": "O(1)"
    },
    "Selection Sort": {
        "Time": "O(n^2)",
        "Best Time": "O(n^2)",
        "Space": "O(1)"
    },
    "Quick Sort": {
        "Time": "O(n^2)",           # Worst-case
        "Best Time": "O(n log n)",  # Average and Best-case
        "Space": "O(log n)"        # Logarithmic space due to the call stack in the worst case
    }
}