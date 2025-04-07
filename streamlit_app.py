import streamlit as st
import utility.api as api

st.set_page_config(
    page_title="Aviation Weather App",
    page_icon="✈️"
)

airport_code = st.text_input("Enter airport code", "KMKE")
st.button("Get Weather!", on_click=lambda: call_api())

# Call the API to get the METAR and TAF data for the specified airport code
def call_api():
    api.get_metar(airport_code)
    api.get_taf(airport_code)