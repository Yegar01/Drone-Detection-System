import cv2
import streamlit as st
from var import variable
from streamlit_webrtc import webrtc_streamer
from st_pages import hide_pages
import av
hide_pages('Live')

model = variable.model.yolo()
conf = variable.value.conf

def video_frame_callback(frame):
    image = frame.to_ndarray(format="bgr24")
    result = model.track(image,persist=True, conf=conf, iou=0.5)
    # if hasattr(result[0].boxes, 'id') and result[0].boxes.id is not None:
    #     variable.warning()
    return av.VideoFrame.from_ndarray(result[0].plot(), format="bgr24")

def live_camera(conf):
    st.write('LIVE CAMERA ON')
    FRAME_WINDOW = st.image([])
    camera = cv2.VideoCapture(0)
    while camera.isOpened():
        _, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = model.track(frame,persist=True,conf=conf,iou=0.5)
        annotated_frame = results[0].plot()
        FRAME_WINDOW.image(annotated_frame)
        if hasattr(results[0].boxes, 'id') and results[0].boxes.id is not None:
            variable.warning()
            break
    else:
        st.write('Stopped')
st.title("Drone Detection System")
st.write("Welcome to our Drone Detection System. This app demonstrates the capabilities of our cutting-edge system for detecting unauthorized drone activity.")
conf = st.sidebar.number_input('Enter Conf. Value',value=conf)
# col1, col2 = st.columns([1,6])
# with col1:
#     run =  st.button('Run')
# with col2:
#     stop = st.button('Stop')
# if run:
#     live_camera(conf=conf)
# if stop and not run:
#     cv2.destroyAllWindows()
webrtc_streamer(
    key="example",
    video_frame_callback=video_frame_callback,
    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
    media_stream_constraints={"video": True, "audio": False},
)
