import streamlit as st
import os
from ultralytics import YOLO

class warning:
    def __init__(self):
        st.warning('Drone has been detected', icon="⚠️")

class value:
    conf = 0.5


class model:
    def __init__(self):
        self.model = YOLO(os.getcwd()+'/best-300e.pt')
    def yolo():
        return YOLO(os.getcwd()+'/best-300e.pt')