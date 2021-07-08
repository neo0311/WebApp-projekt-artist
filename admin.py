import streamlit as st


def uploader():
    user = st.sidebar.text_input('Username')
    passwd = st.sidebar.text_input('Password', type='password')

    if user in ['artist', 'newt'] and passwd in ['artistisawsome', 'newtistoo']:
        st.title(body='Maintenence')
        st.subheader(body='Ahh, So you made it to the admin page, huh?.')
        st.header('Uploader')
    elif user=='' or passwd=='':
        pass
    else:
        st.sidebar.error('Sorry not for you!')
