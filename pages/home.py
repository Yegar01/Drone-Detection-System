import cv2
import streamlit as st
from ultralytics import YOLO
import numpy as np
from PIL import Image
import os

conf=0.5
model = YOLO(os.getcwd()+'/best-300e.pt')

st.session_state.page=1

def warning():
    st.warning('Drone has been detected', icon="⚠️")

def live_camera(run,conf):
    FRAME_WINDOW = st.image([])
    camera = cv2.VideoCapture(1)
    while run:
        _, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = model.track(frame,persist=True,conf=conf,iou=0.5)
        annotated_frame = results[0].plot()
        FRAME_WINDOW.image(annotated_frame)
        if hasattr(results[0].boxes, 'id') and results[0].boxes.id is not None:
            run=False
            warning()
    else:
        st.write('Stopped')
st.title("Drone Detection System")
run = st.checkbox('Run')
st.sidebar.title('Drone Detection System')
uploaded_file = st.sidebar.file_uploader('Upload File',type=['png', 'jpeg', 'jpg'])
conf = st.sidebar.number_input('Enter Conf. Value',value=conf)
if uploaded_file is not None:
    image = np.array(Image.open(uploaded_file))
    result=model.predict(image,conf=conf,iou=0.5)
    st.session_state.image_data = result[0]
    st.image(result[0].plot())

if run == True:
    live_camera(run,conf)