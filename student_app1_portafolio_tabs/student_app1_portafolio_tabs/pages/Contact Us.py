import pandas
import streamlit as st
from send_email import send_email

topics = pandas.read_csv("topics.csv")

with st.form(key="form"):
    email = st.text_input("Your Email Address")
    topic = st.selectbox("What topic do you want to discus?", topics["topic"])
    text = st.text_area("Text")
    button = st.form_submit_button("Submit")

    if button:
        message = f"""\
Subject: New email from {email}

From: {email}
Topic: {topic}
{text}
"""
        send_email(message)
        st.info("Your email was sent successfully")

