# FILE: pages/houses.py
import streamlit as st
import requests

st.title("Dashboard")

# Fetch data from the FastAPI endpoints
response_houses = requests.get("http://127.0.0.1:8000/get-all-houses")
response_ultrasonic = requests.get("http://127.0.0.1:8000/object-distance")
response_infrared = requests.get("http://127.0.0.1:8000/person-side")

# Create a grid layout with 3 columns
col1, col2, col3 = st.columns(3)

# Display houses data in the first column
with col1:
    st.header("Houses Data")
    if response_houses.status_code == 200:
        houses_data = response_houses.json()
        st.write(houses_data)
    else:
        st.error(f"Failed to fetch data: {response_houses.status_code}")

# Display ultrasonic sensor data in the second column
with col2:
    st.header("Ultrasonic Sensor Data")
    if response_ultrasonic.status_code == 200:
        ultrasonic_data = response_ultrasonic.json()
        st.write(ultrasonic_data)
    else:
        st.error(f"Failed to fetch data: {response_ultrasonic.status_code}")

# Display infrared sensor data in the third column
with col3:
    st.header("Infrared Sensor Data")
    if response_infrared.status_code == 200:
        infrared_data = response_infrared.json()
        st.write(infrared_data)
    else:
        st.error(f"Failed to fetch data: {response_infrared.status_code}")