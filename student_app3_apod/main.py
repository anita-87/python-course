import requests
import streamlit as st

api_key = ""
url = "https://api.nasa.gov/planetary/apod?"\
    f"api_key={api_key}&date=2024-03-02"

response = requests.get(url)

apod = response.json()

st.header(apod["title"])
st.image(apod["url"])
st.write(apod["explanation"])
