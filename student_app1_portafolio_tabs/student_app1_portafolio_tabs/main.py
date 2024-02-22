import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.header("The Best Company")

info = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's 
standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type 
specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining 
essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum 
passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
"""
st.write(info)

st.subheader("Our Team")

data = pandas.read_csv("data.csv")

col1, col2, col3 = st.columns(3)

with col1:
    for index, row in data[:4].iterrows():
        name = f"{row['first name'].capitalize()} {row['last name'].capitalize()}"
        st.subheader(name)
        st.write(row["role"])
        st.image(f"images/{row['image']}")

with col2:
    for index, row in data[4:8].iterrows():
        name = f"{row['first name'].capitalize()} {row['last name'].capitalize()}"
        st.subheader(name)
        st.write(row["role"])
        st.image(f"images/{row['image']}")

with col3:
    for index, row in data[8:].iterrows():
        name = f"{row['first name'].capitalize()} {row['last name'].capitalize()}"
        st.subheader(name)
        st.write(row["role"])
        st.image(f"images/{row['image']}")
