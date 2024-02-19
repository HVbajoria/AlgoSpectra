import streamlit as st
import constants as c
import pandas as pd
from utils import (display_all_sorting_algorithms,
                   display_algorithm_type, get_object_from_factory,
                   display_bar_chart)
import numpy as np

def main():

    hide_github_icon = """
            #GithubIcon {
            visibility: hidden;
        }
    """
    # Page layout configurations
    st.set_page_config(page_title="AlgoSpectra", layout="wide", initial_sidebar_state="expanded")

    st.title("🔍 AlgoSpectra")
    
    st.write("""
    Welcome to the **AlgoSpectra**! This tool helps you visualize various sorting algorithms in action.
    Use the dropdown below to select the type of sorting algorithm you'd like to visualize.
    """)
    
    # Create a sidebar for controls and info
    with st.sidebar:
        st.header("Menu")
        algorithm_type = st.selectbox("Algorithm Type:", display_algorithm_type())
        sorting_algorithm = None
        if algorithm_type == c.SORTING_ALGORITHM:
            sorting_algorithm = st.selectbox("Sorting Algorithm:", display_all_sorting_algorithms())
            array_len = st.slider("Array Size:", 5, 100, 20)

    # Main content
    with st.container():
        if not sorting_algorithm:  # If no sorting algorithm is selected
            st.header("Complexities of Common Sorting Algorithms")
            st.write("Below are the complexities of some common sorting algorithms for your reference.")
            df = pd.DataFrame.from_dict(c.ALGORITHM_COMPLEXITIES, orient='index')
            st.table(df)

        elif algorithm_type == c.SORTING_ALGORITHM:
            st.subheader(f"Visualizing: {sorting_algorithm}")
            array = list(np.random.randint(0, 250, array_len))

            if sorting_algorithm:
                display_bar_chart(array, is_initial=True)

                if array:
                    col1, col2, col3 = st.columns([1,1,1])

                    with col2:
                        sort_pressed = st.button("Sort")
                
                if sort_pressed:
                    algorithm_object = get_object_from_factory(sorting_algorithm, c.SORTING_ALGORITHM)
                    algorithm_object.sort(array, callback=algorithm_object.display_bars)
                    st.snow()

if __name__ == "__main__":
    main()

footer="""<style>

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤️ by <a style='display: inline; text-align: center;' href="https://www.linkedin.com/in/harshavardhan-bajoria/" target="_blank">Harshavardhan Bajoria</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)