# Copyright (C) 2025 Nathan Schmitt
# 
import requests
import json
import streamlit as st

# Importing the MetarReport and TafReport classes from the Model package
from Model.METAR import MetarReport
from Model.TAF import TafReport

# Constants for the browser session state keys
SESSION_STATE_METAR_KEY = "metar_data"
SESSION_STATE_TAF_KEY = "taf_data"

# Returns the MetarReport object stored in the browser session state
def get_metar_from_session(): 
    data_str = st.session_state[SESSION_STATE_METAR_KEY]
    return create_metar_report(data_str)

# Returns the TafReport object stored in the browser session state
def get_taf_from_session():
    data_str = st.session_state[SESSION_STATE_TAF_KEY]
    return create_taf_report(data_str)

# Creates a MetarReport object from a JSON string
# The **data_dict[0] syntax is used to unpack the dictionary into keyword arguments
def create_metar_report(data_str):
    if not data_str: return None
    data_dict = json.loads(data_str)
    return MetarReport(**data_dict[0])

# Creates a TafReport object from a JSON string
# The **data_dict[0] syntax is used to unpack the dictionary into keyword arguments
def create_taf_report(data_str):
    if not data_str: return None
    data_dict = json.loads(data_str)
    return TafReport(**data_dict[0])

# Returns the response text from a given URL If the request was successful and not empty
def get_response(url):
    response = requests.get(url)
    if response.status_code == 200 and response.text:
        return response.text.strip()
    return None

# Requests the METAR data from the Aviation Weather API and returns a MetarReport object
# This data is given to us by the Federal Aviation Administration (FAA)
# The METAR (Meteorological Aerodrome Report) is a weather report for a specific airport
def get_metar(airport_code):
    try:
        url = f"https://aviationweather.gov/api/data/metar?ids={airport_code}&format=json"
        data_str = get_response(url)
        st.session_state[SESSION_STATE_METAR_KEY] = data_str
        return create_metar_report(data_str)
    except:
        return None

# Requests the TAF data from the Aviation Weather API and returns a TafReport object
# This data is given to us by the Federal Aviation Administration (FAA)
# The TAF (Terminal Aerodrome Forecast) is a weather forecast for a specific airport
def get_taf(airport_code):
    try:
        url = f"https://aviationweather.gov/api/data/taf?ids={airport_code}&format=json"
        data_str = get_response(url)
        st.session_state[SESSION_STATE_TAF_KEY] = data_str
        return create_taf_report(data_str)
    except:
        return None