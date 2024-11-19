import streamlit as st
from connection import create_connection_aiven
from sensor_ids import get_ids

ultrasonic_id, sound_id, magnetic_id, push_button_id, ir_id = get_ids()


def all_houses():
    connection = create_connection_aiven()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM HOUSE")
    return cursor.fetchall()

def all_persons():
    connection = create_connection_aiven()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM PERSON')
    return cursor.fetchall()
    
def all_rooms():
    connection = create_connection_aiven()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM ROOM')
    return cursor.fetchall()

def all_sensors():
    connection = create_connection_aiven()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM SENSOR')
    return cursor.fetchall()
    
def get_sound_logs():
    connection = create_connection_aiven()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM LOG_SENSOR WHERE sensor_id = 16')
    return cursor.fetchall()
    
def get_magnetic_logs():
    connection = create_connection_aiven()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM LOG_SENSOR WHERE sensor_id = 20')
    return cursor.fetchall()
    
def get_ir_logs():
    connection = create_connection_aiven()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM LOG_SENSOR WHERE sensor_id = 21')
    return cursor.fetchall()
    
def get_ultrasonic_logs():
    connection = create_connection_aiven()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM LOG_SENSOR WHERE sensor_id = 19')
    return cursor.fetchall()
    
def get_push_logs():
    connection = create_connection_aiven()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM LOG_SENSOR WHERE sensor_id = 22')
    return cursor.fetchall()
    
def insert_sensor(sensor_type, unit, room_id):
    connection = create_connection_aiven()
    cursor = connection.cursor()
    query = 'INSERT INTO SENSOR (type_, unit, room_id) VALUES (%s, %s, %s)'
    cursor.execute(query, (sensor_type, unit, room_id))
    connection.commit()
    return {"message": "Sensor inserted successfully."}
    
def insert_house(direction_ip, direction):
    connection = create_connection_aiven()
    cursor = connection.cursor()
    query = 'INSERT INTO HOUSE (direction_ip, direction) VALUES (%s, %s)'
    cursor.execute(query, (direction_ip, direction))
    connection.commit()
    return {"message": "House inserted successfully."}
    
def insert_person(room_id, name):
    connection = create_connection_aiven()
    cursor = connection.cursor()
    query = 'INSERT INTO PERSON (room_id, name) VALUES ((%s, %s)'
    cursor.execute(query, (room_id, name))
    connection.commit()
    return {"message": "House inserted successfully."}
    
def insert_room(room_windows, num_doors):
    connection = create_connection_aiven()
    cursor = connection.cursor()
    query = 'INSERT INTO ROOM (room_windows, num_doors) VALUES (%s, %s)'
    cursor.execute(query, room_windows, num_doors)
    connection.commit()
    return {"message": "Room inserted successfully."}

def insert_log_sensor(date_, measure, sensor_id):
    connection = create_connection_aiven()
    cursor = connection.cursor()
    query = 'INSERT INTO LOG_SENSOR (date_, measure, sensor_id) VALUES (%s, %s, %s)'
    cursor.execute(query, (date_, measure, sensor_id))
    connection.commit()
    return {"message": "Log sensor inserted successfully."}