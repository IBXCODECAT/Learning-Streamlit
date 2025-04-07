import streamlit as st
import pandas as pd
import utility.api as API

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


with st.expander(label="Tempurature and Dewpoint"):
    tempCol0, tempCol1, _ = st.columns(3)

with st.expander(label="Air Pressure"):
    pressureCol0, pressureCol1, _ = st.columns(3)

with st.expander(label="Wind Information"):
    windCol0, windCol1, windCol2 = st.columns(3)

# Cloud Layers
with st.expander(label="Cloud Layers"):
    # Prepare the cloud data for the table
    cloud_data = []
    for cloud in metar.clouds:
        cloud_data.append([cloud.cover, f"{cloud.base}ft", f"{cloud.base - metar.elev}ft"])

    # Create a DataFrame
    cloud_df = pd.DataFrame(cloud_data, columns=["Cover", "Base (MSL)", "Base (AGL)"])

    # Display the table
    st.table(cloud_df)

with st.expander(label="Raw Data", expanded=True):
    st.info(metar.rawOb)
    st.info(taf.rawTAF)

with tempCol0: st.metric(label="Temperature", value=f"{metar.temp}°C", delta_color="off")
with tempCol1: st.metric(label="Dewpoint", value=f"{metar.dewp}°C", delta_color="off")

with pressureCol0: st.metric(label="Sea Level", value=f"{metar.slp}mb", delta_color="off")
with pressureCol1: st.metric(label="Altimeter", value=f"{metar.altim}inHg", delta_color="off")

with windCol0: st.metric(label="Direction", value=f"{metar.wdir}°", delta_color="off")
with windCol1: st.metric(label="Speed:", value=f"{metar.wspd}Kt", delta_color="off")
with windCol2: st.metric(label="Gusts:", value=f"{metar.wgst}Kt", delta_color="off")