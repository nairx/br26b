import sqlite3

conn = sqlite3.connect("app.db")

cursor = conn.cursor()

email = "prem@gmail.com"
password = "1111"

cursor.execute(
    f"""
    update users set password={password}
    where email = '{email}'
    """
)

conn.commit()
conn.close()