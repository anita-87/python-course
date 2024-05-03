import streamlit as st
from  datetime import datetime
import cv2

st.title("Motion Detector")
clicked = st.button("Start Camera")

if clicked:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        now = datetime.now()
        day_of_week = now.strftime('%A')
        time_now = now.strftime("%H:%M:%S")

        cv2.putText(img=frame, text=day_of_week, org=(30, 80), fontFace=cv2.FONT_HERSHEY_PLAIN,
                    fontScale=3, color=(255, 255, 255), thickness=2, lineType=cv2.LINE_AA)
        cv2.putText(img=frame, text=time_now, org=(30, 140), fontFace=cv2.FONT_HERSHEY_PLAIN,
                    fontScale=2, color=(255, 0, 0), thickness=1, lineType=cv2.LINE_AA)

        streamlit_image.image(frame)

