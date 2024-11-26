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

def all_actuators():
    connection = create_connection_aiven()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM ACTUATOR')
    return cursor.fetchall()


def count_persons():
    connection = create_connection_aiven()
    cursor = connection.cursor()
    cursor.execute('SELECT COUNT(*) FROM PERSON')
    return cursor.fetchall()

def count_sensors():
    connection = create_connection_aiven()
    cursor = connection.cursor()
    cursor.execute('SELECT COUNT(*) FROM SENSOR')
    return cursor.fetchall()

def count_rooms():
    connection = create_connection_aiven()
    cursor = connection.cursor()
    cursor.execute('SELECT COUNT(*) FROM ROOM')
    return cursor.fetchall()

def count_houses():
    connection = create_connection_aiven()
    cursor = connection.cursor()
    cursor.execute('SELECT COUNT(*) FROM HOUSE')
    return cursor.fetchall()

def recent_house():
    connection = create_connection_aiven()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM HOUSE ORDER BY house_id DESC LIMIT 1')
    return cursor.fetchall()

def recent_room():
    connection = create_connection_aiven()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM ROOM ORDER BY room_id DESC LIMIT 1')
    return cursor.fetchall()

def recent_sensor():
    connection = create_connection_aiven()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM SENSOR ORDER BY sensor_id DESC LIMIT 1')
    return cursor.fetchall()

def recent_person():
    connection = create_connection_aiven()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM PERSON ORDER BY room_id DESC LIMIT 1')
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
    cursor.execute('SELECT * FROM LOG_SENSOR WHERE sensor_id = 7')
    return cursor.fetchall()
    
def get_ir_logs():
    connection = create_connection_aiven()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM LOG_SENSOR WHERE sensor_id = 11')
    return cursor.fetchall()
    
def get_ultrasonic_logs():
    connection = create_connection_aiven()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM LOG_SENSOR WHERE sensor_id = 6')
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

def insert_actuator(condition, sensor_id):
    connection = create_connection_aiven()
    cursor = connection.cursor()
    query = 'INSERT INTO ACTUATOR (condition_, sensor_id) VALUES (%s, %s)'
    cursor.execute(query, (condition, sensor_id))
    connection.commit()
    return {"message": "Actuator inserted successfully."}
    
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
    query = 'INSERT INTO PERSON (room_id, name) VALUES (%s, %s)'
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

def insert_log_actuator(date_, active_, actuator_id):
    connection = create_connection_aiven()
    cursor = connection.cursor()
    query = 'INSERT INTO LOG_ACTUATOR (date_, active_, actuator_id) VALUES (%s, %s, %s)'
    cursor.execute(query, (date_, active_, actuator_id))
    connection.commit()
    return {"message": "Log actuator inserted successfully."}