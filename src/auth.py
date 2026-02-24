from db_connection import get_db_connection
from email_utils import send_confirmation_email
import hashlib

def validate_login(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    hashed_pass = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute(
        "SELECT * FROM users WHERE username=%s AND password=%s",
        (username, hashed_pass)
    )
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user is not None

def register_user(username, password, email):
    conn = get_db_connection()
    cursor = conn.cursor()
    hashed_pass = hashlib.sha256(password.encode()).hexdigest()

    try:
        cursor.execute(
            "INSERT INTO users (username, password, email) VALUES (%s,%s,%s)",
            (username, hashed_pass, email)
        )
        conn.commit()
        cursor.close()
        conn.close()

        # Send email confirmation
        return send_confirmation_email(email, username)
    except Exception as e:
        print("Registration error:", e)
        return False