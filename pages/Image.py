import streamlit as st
from PIL import Image
import numpy as np
import torch
from var import variable
from st_pages import hide_pages
hide_pages('Image')

model = variable.model.yolo()
conf = variable.value.conf
st.title('Drone Detection System')
st.write("Welcome to our Drone Detection System. This app demonstrates the capabilities of our cutting-edge system for detecting unauthorized drone activity.")
uploaded_file = st.file_uploader('Upload File',type=['png', 'jpeg', 'jpg'])
conf = st.sidebar.number_input('Enter Conf. Value',value=conf)
if uploaded_file is not None:
    image = np.array(Image.open(uploaded_file))
    result=model.predict(image,conf=conf,iou=0.5)
    num = torch.numel(result[0].boxes.cls)
    if hasattr(result[0].boxes, 'id') and num > 0:
        variable.warning()
    st.image(result[0].plot())
    st.write(f'{num} drones have been detected so far')