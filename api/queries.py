import streamlit as st
import pandas as pd
from connection import create_connection

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
    
def all_rooms():
    conn = create_connection()
    if conn:
        df = pd.read_sql('SELECT * FROM ROOM;', conn)
        return df.to_dict()
        conn.close()
    else:
        return {"message": "Failed to connect to the database."}

def all_sensors():
    conn = create_connection()
    if conn:
        df = pd.read_sql('SELECT * FROM SENSOR;', conn)
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
    
def insert_house(direction_ip, direction):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        query = "INSERT INTO HOUSE (direction_ip, direction) VALUES (%s, %s)"
        cursor.execute(query, (direction_ip, direction))
        conn.commit()
        cursor.close()
        conn.close()
        return {"message": "House inserted successfully."}
    else:
        return {"message": "Failed to connect to the database."}
    
def insert_person(room_id, name):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        query = "INSERT INTO PERSON (room_id, name) VALUES (%s, %s)"
        cursor.execute(query, (room_id, name))
        conn.commit()
        cursor.close()
        conn.close()
        return {"message": "Person inserted successfully."}
    else:
        return {"message": "Failed to connect to the database."}
    
def insert_room(room_windows, num_doors):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        query = "INSERT INTO ROOM (room_windows, num_doors) VALUES (%s, %s)"
        cursor.execute(query, (room_windows, num_doors))
        conn.commit()
        cursor.close()
        conn.close()
        return {"message": "Room inserted successfully."}
    else:
        return {"message": "Failed to connect to the database."}

def insert_log_sensor(date_, measure, sensor_id):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
    
        query = "INSERT INTO LOG_SENSOR (date_, measure, sensor_id) VALUES (%s, %s, %s)"
        cursor.execute(query, (date_, measure, sensor_id))
        conn.commit()
        cursor.close()
        conn.close()
        return {"message": "Log sensor inserted successfully."}
    else:
        return {"message": "Failed to connect to the database."}