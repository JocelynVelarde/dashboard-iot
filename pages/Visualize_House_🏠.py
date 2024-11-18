# FILE: visualize.py
import streamlit as st
import requests
import pandas as pd

st.title("Manage my House 🧰")
st.divider()

st.subheader("Add a new sensor 🔧")
# Add sensor information
sensor_type = st.text_input(label="Add the sensor type")
unit = st.text_input(label="Add unit")
room_id = st.number_input(label="Add room id", min_value=int(1), max_value=int(100))
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

st.divider()
st.subheader("Add a new person 👱🏽")
# Add person information
name = st.text_input(label="Person's name")
room_id_person = st.number_input(label="Add room id", min_value=int(1), max_value=int(100), key="person")
if st.button(label='Add person'):
    response_add_person = requests.post("http://127.0.0.1:8000/add-person", json={
        "room_id": room_id_person,
        "name": name,
    })
    if response_add_person.status_code == 200:
        st.success("Person added!")
    else: 
        st.error(f"Failed to add person: {response_add_person.status_code}")

response_houses = requests.get("http://127.0.0.1:8000/get-all-houses")
# Fetch house information
st.divider()
st.subheader('House Information 🏡')
if response_houses.status_code == 200:
    houses_data = response_houses.json()
    df = pd.DataFrame(houses_data)
    st.table(df)  
else:
    st.error(f"Failed to fetch data: {response_houses.status_code}")

response_sensor = requests.get("http://127.0.0.1:8000/get-all-sensors")
# Fetch sensor information
st.divider()
st.subheader('Sensor Information 🧲')
if response_sensor.status_code == 200:
    sensor_data = response_sensor.json()
    df = pd.DataFrame(sensor_data)
    st.table(df)  
else:
    st.error(f"Failed to fetch data: {response_sensor.status_code}")

response_person = requests.get("http://127.0.0.1:8000/get-all-persons")
# Fetch person information
st.divider()
st.subheader('Person Information 🧑‍🧑‍🧒')
if response_person.status_code == 200:
    person_data = response_person.json()
    df = pd.DataFrame(person_data)
    st.table(df)  
else:
    st.error(f"Failed to fetch data: {response_person.status_code}")

response_room = requests.get("http://127.0.0.1:8000/get-all-rooms")
# Fetch room information
st.divider()
st.subheader('Room Information 🚪')
if response_room.status_code == 200:
    room_data = response_room.json()
    df = pd.DataFrame(room_data)
    st.table(df)  
else:
    st.error(f"Failed to fetch data: {response_room.status_code}")




