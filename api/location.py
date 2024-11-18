import streamlit as st
from streamlit_geolocation import streamlit_geolocation

def get_lat_lon():
    location = streamlit_geolocation()
    st.write(location)
    return location
