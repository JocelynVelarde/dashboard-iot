import mysql.connector
from mysql.connector import Error

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