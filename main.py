import streamlit as st
import streamlit.components.v1 as components
from data import Epicurious
import random

TITLE = st.title("recipeo")

USER_INPUT = st.text_input("What are you looking for?")
    
e = Epicurious(USER_INPUT)

while USER_INPUT:
    soup = e.get_soup()
    links = e.get_links(soup)
    srcs = e.filter_links(links)
    i = random.randint(0, len(srcs))
    components.iframe(srcs[i], height=800, scrolling=True)
