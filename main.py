import streamlit as st
import os

st.title("My Streamlit App")

if(os.path.exists("README.md")):
    f = open("README.md", "r")
    content = f.read()
    st.markdown(content)
else:
    st.error("README.md file not found.")