import streamlit as st
import pandas as pd
import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='12345678',
            database='SecureSense'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        st.error(f"Error: {e}")
        return None

conn = create_connection()

if conn:
    df = pd.read_sql('SELECT * FROM HOUSE;', conn)
    st.write(df)
    conn.close()
else:
    st.error("Failed to connect to the database.")