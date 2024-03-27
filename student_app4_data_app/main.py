import streamlit as st
import pandas as pd
import plotly.express as px

st.title("In Search for Happiness")

x_axis = ["GDP", "Happiness", "Generosity"]
x_selected = st.selectbox(options=x_axis, label="Select the data for the X-axis")

y_axis = ["GDP", "Happiness", "Generosity"]
y_selected = st.selectbox(options=y_axis, label="Select the data for the Y-axis")

st.header(f"{x_selected} and {y_selected}")


def get_axis(value):
    match value:
        case "GDP":
            return "gdp"
        case "Happiness":
            return "happiness"
        case "Generosity":
            return "generosity"


def get_data(x_value, y_value):
    df = pd.read_csv("happy.csv")
    x_df = df[get_axis(x_value)]
    y_df = df[get_axis(y_value)]
    return x_df, y_df


x, y = get_data(x_selected, y_selected)
figure = px.scatter(x=x, y=y, labels={"x": f"{x_selected}", "y": f"{y_selected}"})
st.plotly_chart(figure)
