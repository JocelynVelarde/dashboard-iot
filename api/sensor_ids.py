import streamlit as st

def get_ids():
    ultrasonic_id = st.text_input("Sensor ID for ultrasonic sensor")
    sound_id = st.text_input("Sensor ID for sound sensor")
    magnetic_id = st.text_input("Sensor ID for magnetic sensor")
    push_button_id = st.text_input("Sensor ID for push button sensor")
    ir_id = st.text_input("Sensor ID for IR sensor")
    return ultrasonic_id, sound_id, magnetic_id, push_button_id, ir_id
