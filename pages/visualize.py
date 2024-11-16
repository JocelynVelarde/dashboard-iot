# FILE: pages/houses.py
import streamlit as st
import requests

st.title("Houses Data")

response = requests.get("http://127.0.0.1:8000/get-all-houses")

if response.status_code == 200:
    houses_data = response.json()
    st.write(houses_data)
else:
    st.error(f"Failed to fetch data: {response.status_code}")

response = requests.get("http://127.0.0.1:8000/object-distance")

if response.status_code == 200:
    ultrasonic_data = response.json()
    st.write(ultrasonic_data)
else:
    st.error(f"Failed to fetch data: {response.status_code}")

response = requests.get("http://127.0.0.1:8000/person-side")

if response.status_code == 200:
    infrared_data = response.json()
    st.write(infrared_data)
else:
    st.error(f"Failed to fetch data: {response.status_code}")