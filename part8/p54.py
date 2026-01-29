import sqlite3

conn = sqlite3.connect("app.db")

cursor = conn.cursor()

email = "surya@gmail.com"

cursor.execute(
    f"""
    delete from users where email = '{email}'
    """
)
conn.commit()
conn.close()