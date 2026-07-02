import sqlite3
conn = sqlite3.connect("student.db")
cur = conn.cursor()
cur.execute("""CREATE TABLE student (id INTEGER PRIMARY KEY, studentname TEXT, email TEXT, phone INTEGER PRIMAY KEY ) """)
conn.commit()
print("Student table created successfully")
conn.close()