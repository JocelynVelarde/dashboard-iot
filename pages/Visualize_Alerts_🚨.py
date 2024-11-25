import streamlit as st
import requests
import pandas as pd

st.title("Visualize my Alerts 🚨")
st.divider()

st.subheader("Add a new actuator 🔧")
# Add actuator information
actuator_condition = st.number_input(label="Add the actuator condition", min_value=int(1), max_value=int(100))
sensor_id = st.number_input(label="Add sensor id", min_value=int(1), max_value=int(100))
if st.button(label='Add actuator'):
    response_add_actuator = requests.post("https://fast-api-reto.onrender.com/add-actuator", json={
        "condition": actuator_condition,
        "sensor_id_a": sensor_id,
    })
    print(response_add_actuator.text)
    if response_add_actuator.status_code == 200:
        st.success("Actuator added!")
    else: 
        st.error(f"Failed to add actuator: {response_add_actuator.status_code}")
