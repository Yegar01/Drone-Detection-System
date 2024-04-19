import streamlit as st

st.session_state.page = 2

st.title('Drone Detection System')
st.image(st.session_state.image_data[0].plot())