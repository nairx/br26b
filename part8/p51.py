import sqlite3

conn = sqlite3.connect("app.db")

cursor = conn.cursor()

cursor.execute(
    """
    create table IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        password TEXT
    )
    """
)
conn.commit()
conn.close()
