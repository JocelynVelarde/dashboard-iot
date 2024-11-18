import streamlit as st
from streamlit_geolocation import streamlit_geolocation
from geopy.geocoders import Nominatim



def get_lat_lon():
    location = streamlit_geolocation()
    if location:
        latitude = location.get("latitude")
        longitude = location.get("longitude")
        st.write(f"Latitude: {latitude}, Longitude: {longitude}")
        return latitude, longitude
    else:
        st.error("Location data not available")
        return None, None


def get_location():
    latitude, longitude = get_lat_lon()
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(float(latitude)+","+float(longitude))
    return location
    
