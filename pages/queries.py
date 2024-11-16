import streamlit as st
import pandas as pd
from api.connection import create_connection

conn = create_connection()

def get_all_houses():
    if conn:
        df = pd.read_sql('SELECT * FROM HOUSES;', conn)
        return df.to_dict()
        conn.close()
    else:
        return {"message": "Failed to connect to the database."}