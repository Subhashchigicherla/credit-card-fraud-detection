from db_connection import get_connection

conn = get_connection()
if conn.is_connected():
    print("MySQL connection successful!")
    conn.close()
else:
    print("MySQL connection failed!")