import streamlit as st
from Components.component import my_component

st.title("Test Custom Component")

result = my_component(name="Commander Schmitt")
st.write("Result from component:", result)
