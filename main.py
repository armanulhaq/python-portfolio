import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Arman Ul Haq")
    st.info("I am a passionate Python developer eager to learn and create innovative projects. With a deep interest in problem-solving and continuous learning, I enjoy exploring new technologies and applying them to real-world challenges. My journey involves pushing boundaries to enhance my skills and develop impactful solutions.")

content2 = "Below you can find some of the apps I have built in Python. Feel free to contact me!"
st.write(content2)


col3, col4 = st.columns(2)
df=pd.read_csv('data.csv', sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
