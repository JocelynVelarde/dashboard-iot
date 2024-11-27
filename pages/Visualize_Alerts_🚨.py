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

st.divider()
st.subheader("Actuator Information")
response_actuator = requests.get("https://fast-api-reto.onrender.com/get-all-actuators")
if response_actuator.status_code == 200:
    actuator_data = response_actuator.json()
    df = pd.DataFrame(actuator_data)
    st.table(df)  
else:
    st.error(f"Failed to fetch data: {response_actuator.status_code}")

st.divider()
st.subheader("LCD Alerts")
response_lcd = requests.get("https://fast-api-reto.onrender.com/get-lcd-logs")
if response_lcd.status_code == 200:
    lcd_data = response_lcd.json()
    df = pd.DataFrame(lcd_data)
    st.table(df)  
else:
    st.error(f"Failed to fetch data: {response_lcd.status_code}")

st.divider()
st.subheader("Vibration Alerts")
response_vibration = requests.get("https://fast-api-reto.onrender.com/get-vibration-logs")
if response_vibration.status_code == 200:
    vibration_data = response_vibration.json()
    df = pd.DataFrame(vibration_data)
    st.table(df)
else:
    st.error(f"Failed to fetch data: {response_vibration.status_code}")

st.divider()
st.subheader("LED Alerts")
response_led = requests.get("https://fast-api-reto.onrender.com/get-led-logs")
if response_led.status_code == 200:
    led_data = response_led.json()
    df = pd.DataFrame(led_data)
    st.table(df)
else:
    st.error(f"Failed to fetch data: {response_led.status_code}")

st.divider()
st.subheader("Servo Alerts")
response_servo = requests.get("https://fast-api-reto.onrender.com/get-servo-logs")
if response_servo.status_code == 200:
    servo_data = response_servo.json()
    df = pd.DataFrame(servo_data)
    st.table(df)
else:
    st.error(f"Failed to fetch data: {response_servo.status_code}")

st.divider()
st.subheader("Buzzer Alerts")
response_buzzer = requests.get("https://fast-api-reto.onrender.com/get-buzzer-logs")
if response_buzzer.status_code == 200:
    buzzer_data = response_buzzer.json()
    df = pd.DataFrame(buzzer_data)
    st.table(df)
else:
    st.error(f"Failed to fetch data: {response_buzzer.status_code}")