import psycopg2
import hashlib
from config.app_config import DB_CONFIG

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(email, password):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO users (email, password) VALUES (%s, %s)",
            (email, hash_password(password))
        )
        conn.commit()
        return True
    except psycopg2.errors.UniqueViolation:
        conn.rollback()
        return False
    finally:
        cur.close()
        conn.close()

def authenticate_user(email, password):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute(
        "SELECT password FROM users WHERE email = %s",
        (email,)
    )
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row and row[0] == hash_password(password):
        return True
    return False 