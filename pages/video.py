import cv2
import streamlit as st
from ultralytics import YOLO
from st_pages import hide_pages
hide_pages('video')

def app():
    st.header('Object Detection Web App')
    st.subheader('Powered by YOLOv8')
    st.write('Welcome!')
    model = YOLO('yolov8n.pt')

    with st.form("my_form"):
        uploaded_file = st.file_uploader("Upload video", type=['mp4'])
        st.form_submit_button(label='Submit')

    if uploaded_file is not None: 
        input_path = uploaded_file.name
        file_binary = uploaded_file.read()
        with open(input_path, "wb") as temp_file:
            temp_file.write(file_binary)
            
if __name__ == "__main__":
    app()