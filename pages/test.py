import streamlit as st
import pandas as pd
from api.connection import create_connection

conn = create_connection()

if conn:
    df = pd.read_sql('SELECT * FROM SENSOR;', conn)
    st.write(df)
    conn.close()
else:
    st.error("Failed to connect to the database.")