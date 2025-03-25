import streamlit as st
import Utility.API as API

metar = API.get_metar_from_session()
taf = API.get_taf_from_session()

st.header(metar.name)

with st.expander("Airport Location"):
    st.write(f"Latitude: {metar.lat}, Longitude: {metar.lon}")
    st.write(f"Elevation: {metar.elev} ft")
    st.map(
        data=[{"lat": metar.lat, "lon": metar.lon}],
        latitude=metar.lat,
        longitude=metar.lon,
        zoom=12)


with st.expander("Tempurature"):
    st.write(f"Temperature: {metar.temp}°C")
    st.write(f"Dewpoint: {metar.dewp}°C")
    
with st.expander("Wind Observation"):
    st.write(f"Wind Direction: {metar.wdir}° True")
    st.write(f"Wind Speed: {metar.wspd} kt")
    st.write(f"Gusts: {metar.wgst} kt")