import qrcode
import sqlite3

conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        student_id TEXT UNIQUE NOT NULL
    )
''')

students = [("Luis", "LuisQR"), ("Heesung", "HeesungQR"),("Duane","DUANEQR")]
cursor.executemany("INSERT OR IGNORE INTO students (name, student_id) VALUES (?, ?)", students)
conn.commit()

for name, student_id in students:
    qr = qrcode.make(student_id)
    qr.save(f"{student_id}.png") 

print("QR Codes generated.")
conn.close()
