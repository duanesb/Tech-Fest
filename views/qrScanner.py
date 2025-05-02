import base64
from datetime import datetime, timedelta
import threading
import cv2
import flet as ft
from objects import appWidth,appHeight,ElevatedButton,TextField
import sqlite3

def qrScannerContent():
    def captureLoop():
        cap = cv2.VideoCapture(0)
        detector = cv2.QRCodeDetector()
        while True:
            ret, rawQR = cap.read()
            if not ret:
                continue

            # TRANSFORM VIDEO
            _, buf = cv2.imencode(".png", rawQR)
            b64 = base64.b64encode(buf).decode()
            video.src_base64 = b64
            video.update()

            # READ QR
            invertedQR = cv2.bitwise_not(rawQR)
            rawData = detector.detectAndDecode(invertedQR)
            qrStudentID = rawData[0]

            if qrStudentID:
                # MARK THE ATTENDANCE
                conn = sqlite3.connect("storage.db")
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM students WHERE student_id = ?", (qrStudentID,))
                qrMatchStudent = cursor.fetchone()
                print(qrMatchStudent)
                if qrMatchStudent:
                    qrMatchName = qrMatchStudent[1]
                    now = datetime.now()

                    # CHECK IF ONE MINUTE HAS PASSED AFTER LAST REGISTRATION OF THE SAME QR
                    cursor.execute(
                        "SELECT MAX(timestamp) FROM attendance WHERE student_id = ?",
                        (qrStudentID,)
                    )
                    last = cursor.fetchone()[0]
                    if last:
                        last_dt = datetime.strptime(last, "%Y-%m-%d %H:%M:%S")
                        if now - last_dt < timedelta(minutes=1):
                            conn.close()
                            continue
                    
                    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
                    print(qrMatchName)
                    cursor.execute(
                        "INSERT INTO attendance (student_id, name, timestamp) VALUES (?, ?, ?)",
                        (qrStudentID, qrMatchName, timestamp)
                    )
                    print(f"Inserted at timestamp: {timestamp}")
                    conn.commit()
                conn.close()
    
    threading.Thread(target=captureLoop, daemon=True).start()    
    video = ft.Image(src_base64="", width=appWidth, height=appHeight-110, fit=ft.ImageFit.COVER)
    idField = TextField("Last Scanned ID", lambda e: None)
    idField.value = ""
    idField.visible = False

    content = ft.Container(
        width=appWidth,
        height=appHeight,
        content=ft.Column(
            spacing=10,
            alignment=ft.MainAxisAlignment.START,
            controls=[
                video,
                ft.Row(
                    controls=[
                        ElevatedButton("Return Home",lambda _:_.page.go("/home")),
                        ElevatedButton("View Attendance", lambda _:_.page.go("/attendance"))
                    ]
                )
            ]
        )
    )
    return content