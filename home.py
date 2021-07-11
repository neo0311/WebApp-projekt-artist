import streamlit as st
import os


def home(layout_data=None):
    st.title(layout_data["home_title"])
    st.subheader(layout_data["home_subheader"])
    if os.path.isfile('resources/home.jpeg'):
        column =st.beta_columns(1)
        column[0].image('resources/home.jpeg', width=500)