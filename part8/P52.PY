import sqlite3

conn = sqlite3.connect("app.db")

cursor = conn.cursor()

cursor.execute(
    """
    insert into users(name,email,password)
    values('Prem','prem@gmail.com','1234')
    """
)

conn.commit()
conn.close()