import flet as ft
import sqlite3

def main(page: ft.Page):
    page.title = "QR Code Attendance System"
    
    def load_attendance():
        conn = sqlite3.connect("attendance.db")
        cursor = conn.cursor()
        cursor.execute("SELECT name, timestamp FROM attendance")
        records = cursor.fetchall()
        conn.close()
        
        attendance_list.controls.clear()
        for record in records:
            name, timestamp = record
            attendance_list.controls.append(ft.ListTile(title=ft.Text(name), subtitle=ft.Text(timestamp)))
        page.update()

    attendance_list = ft.ListView(expand=True)
    page.add(ft.Text("Attendance Records", size=20), attendance_list)
    load_attendance()

ft.app(target=main)
