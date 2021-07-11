import streamlit as st
import os

def show_writings(layout_data=None):
    """
    Renders the writings page

    Parameters
    ----------

    layout_data: dictionary with info about the layout of page

    """
    from main import read_imgs, arrange_imgs
    st.title(body=layout_data["writings_title"])
    st.subheader(body=layout_data["writings_subheader"])
    path='resources' + os.sep + 'writings' + os.sep + '*.*'
    imgs = read_imgs(path)
    arrange_imgs(image=imgs, st=st, layout_data=layout_data)