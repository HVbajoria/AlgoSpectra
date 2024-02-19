import constants as c
import streamlit as st
import random
from src.sorting.sort_factory import SortFactory
from src.searching.search_factory import SearchFactory
import time

def display_all_sorting_algorithms():
    return ["",c.BUBBLE_SORT, c.INSERTION_SORT, c.SELECTION_SORT, c.MERGE_SORT, c.QUICK_SORT]

def display_all_searching_algorithms():
    return ["",c.BINARY_SEARCH, c.LINEAR_SEARCH, c.INTERPOLATION_SEARCH, c.INTERPOLATION_SEARCH]

def display_algorithm_type() -> list:
    return [c.SORTING_ALGORITHM]

def get_object_from_factory(algorithm_name, algorithm_type):
    if algorithm_type == c.SORTING_ALGORITHM:
        return SortFactory.get_object(algorithm_name)
    elif algorithm_type == c.SEARCHING_ALGORITHM:
        return SearchFactory.get_object(algorithm_name)
    else:
        raise ValueError('Invalid Selection')

def display_bar_chart(array, sub_array=None, is_initial=False, is_merge=False):
    """
    Display a bar chart in Streamlit.
    
    Parameters:
    - array (list): The main array.
    - sub_array (list): A sub array, if present.
    - is_initial (bool): Flag to check if it's the initial plot.
    - is_merge (bool): Flag to check if it's a merge operation.
    """
    # Check if it's an initial plot
    if is_initial:
        st.session_state.plot_placeholder = st.empty()
        st.session_state.plot_placeholder.bar_chart(array)
        return
    
    # Update the bar chart
    if not is_merge:
        st.session_state.plot_placeholder.bar_chart(array)
    else:
        processed_array = create_gapped_array(array, sub_array) if sub_array else array
        st.session_state.plot_placeholder.bar_chart(processed_array)
    
    time.sleep(0.05)

@st.cache_resource
def create_gapped_array(array, sub_array):
    """
    Create a new array with zeros for elements present in the sub_array.
    
    Parameters:
    - array (list): The main array.
    - sub_array (list): The sub array.
    
    Returns:
    - list: The gapped array.
    """
    gapped_array = [0 if value in sub_array else value for value in array]
    return gapped_array