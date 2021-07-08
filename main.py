import numpy as np
import pandas as pd
import cv2
import streamlit as st
from home import home
from admin import uploader

def start():
    
    select = st.sidebar.selectbox(label="Choose one", options=('Home', 'Drawings', 
                                    'Stencils', 'Photos', 'Writings', 'admin'))
    if select == 'Home':
        home()
    elif select == 'Drawings':
        st.title('Drawings')
    elif select == 'Stencils':
        st.header('Stencils')
    elif select == 'Photos':
        st.header('Photos')
    elif select == 'Writings':
        st.header('Writings')
    elif select == 'admin':
        uploader()

if __name__ == "__main__":
    start()