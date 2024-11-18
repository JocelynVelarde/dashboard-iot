# FILE: visualize.py
import streamlit as st
import requests

st.title("Dashboard")

sensor_type = st.text_input(label="Add the sensor type")
unit = st.text_input(label="Add unit")
room_id = st.number_input(label="Add room id", min_value=int(1), max_value=int(100))

# Fetch data from the FastAPI endpoints
response_houses = requests.get("http://127.0.0.1:8000/get-all-houses")

if st.button(label='Add sensor'):
    response_add_sensor = requests.post("http://127.0.0.1:8000/add-sensor", json={
        "type_": sensor_type,
        "unit": unit,
        "room_id": room_id
    })
    if response_add_sensor.status_code == 200:
        st.success("Sensor added!")
    else: 
        st.error(f"Failed to add sensor: {response_add_sensor.status_code}")

if response_houses.status_code == 200:
    houses_data = response_houses.json()
    st.write(houses_data)
else:
    st.error(f"Failed to fetch data: {response_houses.status_code}")




