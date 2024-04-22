import streamlit as st
import os

st.page_link(os.getcwd()+'/pages/home.py',label='home')
st.page_link(os.getcwd()+'/pages/user.py',label='user')
