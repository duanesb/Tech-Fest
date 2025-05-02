import flet as ft
import sqlite3
from objects import appWidth, appHeight, ElevatedButton

def fetch_students():
    conn = sqlite3.connect("storage.db")
    cursor = conn.cursor()

    # Pull all student entries
    cursor.execute("SELECT student_id, name FROM students ORDER BY name")
    records = cursor.fetchall()
    conn.close()

    return records

def EntriesContent():
    students = fetch_students()

    # Build a scrollable list of students (ID and name only), black and bold text
    student_list = [
        ft.Text(
            f"{i+1}. {student_id} — {name}",
            color=ft.colors.BLACK,
            weight=ft.FontWeight.BOLD
        )
        for i, (student_id, name) in enumerate(students)
    ]

    content = ft.Container(
        width=appWidth,
        height=appHeight,
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ElevatedButton("Return Home", lambda _: _.page.go("/home")),
                        ElevatedButton("Select", None),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Divider(),
                ft.Text(
                    "Registered Students",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.BLACK
                ),
                ft.Column(
                    controls=student_list,
                    scroll=ft.ScrollMode.AUTO,
                    expand=True
                ),
            ]
        )
    )
    return content
