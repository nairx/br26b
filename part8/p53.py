import sqlite3

conn = sqlite3.connect("app.db")

cursor = conn.cursor()

cursor.execute(f"select * from users")

rows = cursor.fetchall()

for row in rows:
    print(row)

# email = "surya@gmail.com"
# cursor.execute(f"select * from users where email = '{email}'")
# user = cursor.fetchone()
# print(user)

cursor.close()
conn.close()