import streamlit as st
import os
st.markdown("""
    <style>
        section[data-testid="stSidebar"][aria-expanded="true"]{
            display: none;
        }
    </style>
    """, unsafe_allow_html=True)

st.title('Drone Detection System')
st.subheader('Select the following through which you want to perform detection')

col1, col2 = st.columns([1,250])
with col2:
    st.page_link(os.getcwd()+'/pages/Live.py',label='Live Camera')
with col1:
    st.write(':one:')
col1, col2 = st.columns([1,250])
with col1:
    st.write(':two:')
with col2:
    st.page_link(os.getcwd()+'/pages/Image.py',label='Images')