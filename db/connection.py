# db/connection.py
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "users.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT
        )
    """)
    conn.commit()
    conn.close()

def user_exists(username: str) -> bool:
    conn = get_connection()
    cursor = conn.execute("SELECT 1 FROM users WHERE username = ?", (username,))
    exists = cursor.fetchone() is not None
    conn.close()
    return exists

# Crea la tabla al importar el módulo
create_table()