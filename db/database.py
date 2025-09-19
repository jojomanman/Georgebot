import sqlite3
import logging

logger = logging.getLogger(__name__)

def log_message(chat_id, user_id, text, timestamp, is_response=False):
    conn = sqlite3.connect('bot_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chat_id INTEGER,
            user_id INTEGER,
            message_text TEXT,
            timestamp TEXT,
            is_response BOOLEAN DEFAULT FALSE
        )
    ''')
    cursor.execute('''
        INSERT INTO messages (chat_id, user_id, message_text, timestamp, is_response)
        VALUES (?, ?, ?, ?, ?)
    ''', (chat_id, user_id, text, timestamp, is_response))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id
def log_response(chat_id, user_id, text, timestamp):
    return log_message(chat_id, user_id, text, timestamp, is_response=True)

def log_location(chat_id, user_id, lat, long, timestamp):
    conn = sqlite3.connect('bot_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS locations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chat_id INTEGER,
            user_id INTEGER,
            latitude REAL,
            longitude REAL,
            timestamp TEXT
        )
    ''')
    cursor.execute('''
        INSERT INTO locations (chat_id, user_id, latitude, longitude, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (chat_id, user_id, lat, long, timestamp))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id