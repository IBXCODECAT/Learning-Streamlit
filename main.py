import streamlit as st
import Utility.API as API

st.set_page_config(
    page_title="Aviation Weather App",
    page_icon="✈️"
)

airport_code = st.text_input("Enter airport code", "KMKE")
st.button("Get Weather!")

st.button("Get METAR", on_click=lambda: call_api)

def call_api():
    API.get_metar(airport_code)
    API.get_taf(airport_code)