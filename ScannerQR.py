import cv2
import sqlite3
from pyzbar.pyzbar import decode
from datetime import datetime

def scan_qr():
    cap = cv2.VideoCapture(0)
    
    while True:
        _, frame = cap.read()
        for barcode in decode(frame):
            student_id = barcode.data.decode("utf-8")
            mark_attendance(student_id)
            cap.release()
            cv2.destroyAllWindows()
            return student_id
        
        cv2.imshow("QR Scanner", frame)
        if cv2.waitKey(1) == 27: 
            break
    
    cap.release()
    cv2.destroyAllWindows()

def mark_attendance(student_id):
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT name FROM students WHERE student_id = ?", (student_id,))
    student = cursor.fetchone()
    
    if student:
        name = student[0]
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS attendance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT NOT NULL,
                name TEXT NOT NULL,
                timestamp TEXT NOT NULL
            )
        ''')
        
        cursor.execute("INSERT INTO attendance (student_id, name, timestamp) VALUES (?, ?, ?)", 
                       (student_id, name, date))
        conn.commit()
        print(f"Attendance marked for {name} at {date}")
    else:
        print("Student not found!")
    
    conn.close()

scan_qr()
