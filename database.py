import sqlite3
from config import DB_NAME
class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self._create_tables()

    def _get_connection(self):
        conn = sqlite3.connect(self.db_name)
        return conn

    def _create_tables(self):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Groups (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                group_name TEXT NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Lessons (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                lesson_name TEXT NOT NULL,
                lesson_time TEXT NOT NULL,
                lesson_day TEXT NOT NULL,
                group_id INTEGER,
                FOREIGN KEY (group_id) REFERENCES Groups(id)
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                group_id INTEGER,
                subscription_date TEXT,
                FOREIGN KEY (group_id) REFERENCES Groups(id)
            )
        """)
        conn.commit()
        conn.close()

    def add_user(self, user_id, username):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO Users (user_id, username, subscription_date) VALUES (?, ?, datetime('now'))",
                      (user_id, username))
        conn.commit()
        conn.close()

    def set_user_group(self, user_id, group_id):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Users SET group_id = ? WHERE user_id = ?", (group_id, user_id))
        conn.commit()
        conn.close()

    def get_user_group(self, user_id):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT group_id FROM Users WHERE user_id = ?", (user_id,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None

    def get_groups(self):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, group_name FROM Groups")
        result = cursor.fetchall()
        conn.close()
        return result

    def get_schedule(self, group_id):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT lesson_name, lesson_time, lesson_day FROM Lessons WHERE group_id = ?", (group_id,))
        result = cursor.fetchall()
        conn.close()
        return result

    def close(self):
        pass

