import plotly.express as px
import pandas
import streamlit as st

df = pandas.read_csv("data.csv")

figure = px.line(x=df["date"], y=df["temperature"], labels={"x": "Date", "y": "Temperature (C)"})

st.title("Temperatures")
st.plotly_chart(figure)
