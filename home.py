import streamlit as st


def home():
    st.title("My Gallary")
    st.subheader('Just a collection of (almost) all of my works.')
    st.image('resources/home.jpeg', use_column_width=True)