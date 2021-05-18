import streamlit as st
import streamlit.components.v1 as components
from data import Epicurious
import random

TITLE = st.title("recipeo")

USER_INPUT = st.text_input("What are you looking for?")
    
e = Epicurious("chicken")
soup = e.get_soup()
links = e.get_links(soup)
srcs = e.filter_links(links)

if USER_INPUT:
    try:
        i = random.randint(0, len(srcs))
        components.iframe(srcs[i], height=800, scrolling=True)
    except IndexError:
        st.write("Search for something else.")
