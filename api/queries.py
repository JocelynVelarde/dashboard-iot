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