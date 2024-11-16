import streamlit as st
import pandas as pd
import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host=st.secrets["db_host"],
            user=st.secrets["db_user"],
            password=st.secrets["db_password"],
            database=st.secrets["db_name"]
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