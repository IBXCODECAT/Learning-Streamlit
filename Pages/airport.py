import streamlit as st
import Utility.API as API

metar = st.session_state["metar_data"] if "metar_data" in st.session_state else None
taf = st.session_state["taf_data"] if "taf_data" in st.session_state else None

def show_metar():
    st.area_chart([metar.temp, metar.dewp])
    st.write(f"METAR for {metar.icaoId} at {metar.reportTime}")
    st.write(f"Temperature: {metar.temp}°C")
    st.write(f"Dewpoint: {metar.dewp}°C")
    st.write(f"Wind: {metar.wdir}° @ {metar.wspd}kt")
    st.write(f"Visibility: {metar.visib}m")
    st.write(f"Altimeter: {metar.altim}inHg")
    st.write(f"Clouds: {', '.join([str(cloud) for cloud in metar.clouds])}")

def show_taf():
    st.write(f"TAF for {taf.icaoId} from {taf.validTimeFrom} to {taf.validTimeTo}")
    st.write(f"Raw TAF: {taf.rawTAF}")
    
    for forecast in taf.fcsts:
        st.write(f"\nForecast Group {forecast.timeGroup}:")
        st.write(f"  Time: {forecast.timeFrom} to {forecast.timeTo}")
        st.write(f"  Wind: {forecast.wdir}° @ {forecast.wspd}kt")
        st.write(f"  Visibility: {forecast.visib}")
        st.write(f"  Clouds: {', '.join([f'{cloud.cover} at {cloud.base}ft' for cloud in forecast.clouds])}")
        
        if forecast.fcstChange:
            st.write(f"  Forecast change: {forecast.fcstChange}")
        if forecast.probability:
            st.write(f"  Probability: {forecast.probability}%")

show_metar()
show_taf()