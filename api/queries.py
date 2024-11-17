import streamlit as st
import pandas as pd
from connection import create_connection
import datetime

def all_houses():
    conn = create_connection()
    if conn:
        df = pd.read_sql('SELECT * FROM HOUSE;', conn)
        return df.to_dict()
        conn.close()
    else:
        return {"message": "Failed to connect to the database."}

def all_persons():
    conn = create_connection()
    if conn:
        df = pd.read_sql('SELECT * FROM PERSON;', conn)
        return df.to_dict()
        conn.close()
    else:
        return {"message": "Failed to connect to the database."}


def insert_sensor(sensor_type, unit, room_id):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        query = "INSERT INTO SENSOR (type_, unit, room_id) VALUES (%s, %s, %s)"
        cursor.execute(query, (sensor_type, unit, room_id))
        conn.commit()
        cursor.close()
        conn.close()
        return {"message": "Sensor inserted successfully."}
    else:
        return {"message": "Failed to connect to the database."}

# FILE: queries.py
def insert_log_sensor(date_, measure, sensor_id):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query = "INSERT INTO LOG_SENSOR (date_, measure, sensor_id) VALUES (%s, %s, %s)"
        cursor.execute(query, (current_time, measure, sensor_id))
        conn.commit()
        cursor.close()
        conn.close()
        return {"message": "Log sensor inserted successfully."}
    else:
        return {"message": "Failed to connect to the database."}