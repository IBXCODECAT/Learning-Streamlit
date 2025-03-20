import streamlit as st
import os

st.title("Exploring Streamlit")
st.divider()
st.button("Show README", on_click=lambda: show_readme())

def show_readme():
    try:
        with open("README.md", "r") as f:
            content = f.read()
        st.markdown(content)
    except FileNotFoundError:
        st.exception(FileNotFoundError("README.md file not found."))