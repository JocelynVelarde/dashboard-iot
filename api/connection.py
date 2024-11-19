import mysql.connector
import streamlit as st
from mysql.connector import Error
import pymysql

def create_connection():
    try:
        connection = mysql.connector.connect(
            host=st.secrets["db_host"],
            user=st.secrets["db_username"],
            password=st.secrets["db_password"],
            database=st.secrets["db_database"]
        )
        if connection.is_connected():
            return connection
    except Error as e:
        st.error(f"Error: {e}")
        return None
    
def create_connection_aiven():
    timeout = 10
    connection = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db="SecureSense",
    host=st.secrets["aiven_host"],
    password=st.secrets["aiven_password"],
    read_timeout=timeout,
    port=st.secrets["aiven_port"],
    user=st.secrets["aiven_user"],
    write_timeout=timeout,
)
    return connection