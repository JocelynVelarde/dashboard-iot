# FILE: visualize.py
import streamlit as st
import requests

st.title("Dashboard")

# Fetch data from the FastAPI endpoints
response_houses = requests.get("http://127.0.0.1:8000/get-all-houses")
response_ultrasonic = requests.get("http://127.0.0.1:8000/object-distance")
response_infrared = requests.get("http://127.0.0.1:8000/person-side")

# Create a grid layout with 3 columns
col1, col2, col3 = st.columns(3)

# Function to convert data to HTML table
def convert_to_html_table(data):
    if isinstance(data, list):
        keys = data[0].keys()
        table = "<table><thead><tr>" + "".join([f"<th>{key}</th>" for key in keys]) + "</tr></thead><tbody>"
        for item in data:
            table += "<tr>" + "".join([f"<td>{item[key]}</td>" for key in keys]) + "</tr>"
        table += "</tbody></table>"
        return table
    elif isinstance(data, dict):
        table = "<table><tbody>"
        for key, value in data.items():
            table += f"<tr><td>{key}</td><td>{value}</td></tr>"
        table += "</tbody></table>"
        return table
    return ""

# Display houses data in the first column
with col1:
    st.header("Houses Data")
    if response_houses.status_code == 200:
        houses_data = response_houses.json()
        houses_table = convert_to_html_table(houses_data)
        st.markdown(houses_table, unsafe_allow_html=True)
    else:
        st.error(f"Failed to fetch data: {response_houses.status_code}")

# Display ultrasonic sensor data in the second column
with col2:
    st.header("Ultrasonic Sensor Data")
    if response_ultrasonic.status_code == 200:
        ultrasonic_data = response_ultrasonic.json()
        ultrasonic_table = convert_to_html_table([ultrasonic_data])
        st.markdown(ultrasonic_table, unsafe_allow_html=True)
    else:
        st.error(f"Failed to fetch data: {response_ultrasonic.status_code}")

# Display infrared sensor data in the third column
with col3:
    st.header("Infrared Sensor Data")
    if response_infrared.status_code == 200:
        infrared_data = response_infrared.json()
        infrared_table = convert_to_html_table([infrared_data])
        st.markdown(infrared_table, unsafe_allow_html=True)
    else:
        st.error(f"Failed to fetch data: {response_infrared.status_code}")