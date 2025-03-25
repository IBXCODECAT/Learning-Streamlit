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
    return st.session_state[SESSION_STATE_METAR_KEY] if "metar_data" in st.session_state else None

# Returns the TafReport object stored in the browser session state
def get_taf_from_session():
    return st.session_state[SESSION_STATE_TAF_KEY] if "taf_data" in st.session_state else None

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
        data_dict = json.loads(data_str)

        # Creating a MetarReport object from the data
        # The **data_dict[0] syntax is used to unpack the dictionary into keyword arguments
        metar_report = MetarReport(**data_dict[0])

        # Store the MetarReport object in the browser session state
        st.session_state[SESSION_STATE_METAR_KEY] = metar_report
        return metar_report
    except:
        # Wipe the MetarReport object from the browser session state if the request fails
        st.session_state[SESSION_STATE_TAF_KEY] = None
        return None

# Requests the TAF data from the Aviation Weather API and returns a TafReport object
# This data is given to us by the Federal Aviation Administration (FAA)
# The TAF (Terminal Aerodrome Forecast) is a weather forecast for a specific airport
def get_taf(airport_code):
    try:
        url = f"https://aviationweather.gov/api/data/taf?ids={airport_code}&format=json"
        data_str = get_response(url)
        data_dict = json.loads(data_str)
        
        # Creating a TafReport object from the data
        # The **data_dict[0] syntax is used to unpack the dictionary into keyword arguments
        taf_report = TafReport(**data_dict[0])

        # Store the TafReport object in the browser session state
        st.session_state["taf_data"] = taf_report
        return taf_report
    except:
        # Wipe the TafReport object from the browser session state if the request fails
        st.session_state["taf_data"] = None
        return None