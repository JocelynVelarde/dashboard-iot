# FILE: visualize.py
import streamlit as st
import requests
import pandas as pd
from api.location import get_location

st.title("Manage my House 🧰")
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

st.divider()

st.subheader("Add a new room 🪟")
# Add room information
num_windows = st.number_input(label="Add number of windows", min_value=int(1), max_value=int(100), key="windows")
num_doors = st.number_input(label="Add number of doors", min_value=int(1), max_value=int(100), key="doors")
if st.button(label='Add room'):
    response_add_room = requests.post("http://127.0.0.1:8000/add-room", json={
        "num_windows": num_windows,
        "num_doors": num_doors,
    })
    if response_add_room.status_code == 200:
        st.success("Room added!")
    else: 
        st.error(f"Failed to add room: {response_add_room.status_code}")

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

st.divider()
st.subheader("Add a new house 🌳")
st.write("If location unkown use the tool below to find your location")
location = get_location()
st.write(location)
# Add house information
direction_ip = st.text_input(label="IP Direction")
direction = st.text_input(label="Direction")
if st.button(label='Add house'):
    response_add_house = requests.post("http://127.0.0.1:8000/add-house", json={
        "direction_ip": direction_ip,
        "direction": direction,
    })
    if response_add_house.status_code == 200:
        st.success("House added!")
    else: 
        st.error(f"Failed to add house: {response_add_house.status_code}")

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




